#!/usr/bin/python
import numpy as np
import ezgal,cgi,re,os,sys,time
import _mysql_exceptions as _mysql

print 'Content-type: text/plain';

# load form results
form = cgi.FieldStorage()

# check that all necessary fields have been passed
if 'model' not in form:
	print
	print 'You must choose the model set in the "Model" tab'
	sys.exit()

if 'sfh' not in form:
	print
	print 'You must choose a SFH in the "Model" tab'
	sys.exit()

if form['sfh'].value != 'SSP' and form['sfh'].value + '_tau' not in form:
	print
	if form['sfh'].value == 'Constant':
		print 'You must choose a V-band optical depth in the "Model" tab'
	else:
		print 'You must choose a burst time scale in the "Model" tab %s'
	sys.exit()

# first we have to figure out which file to load

# model set
file = form['model'].value.lower() + '_'

# sfh
if form['sfh'].value == 'Burst':
	file += 'burst'
elif form['sfh'].value == 'SSP':
	file += 'ssp'
else:
	file += 'exp'

# tau
tau_val = ''
if form['sfh'].value != 'SSP':
	tau_val = form[form['sfh'].value + '_tau'].value
	file += '_%s' % tau_val

# metallicity
file += '_z_%s' % form['met'].value

# imf
file += '_'
imf_val = form[form['model'].value + '_imf'].value
if imf_val == 'Chabrier':
	file += 'chab'
elif imf_val == 'Salpeter':
	file += 'salp'
elif imf_val == 'Kroupa':
	file += 'krou'

# finally the folder and extension
file = 'models/%s.ascii' % file

# now make sure the file exists - quit otherwise
if not os.path.isfile( file ):
	print 'That is not a valid choice of model parameters!  Please try again.'
	sys.exit()

# okay, now load the model
model = ezgal.ezgal_light( file )

# check for valid formation redshift
zf = float( form['zf'].value )
if np.abs( model.zfs-zf ).min() > model.tol:
	print
	print 'That is not a valid formation redshift!  Please try again.'
	sys.exit()

# and check for valid filters
if 'filters' not in form:
	print
	print 'You must select a filter!'
	sys.exit()

filters = []
if type( form['filters'] ) == type( [] ):
	for filter in form['filters']:
		filters.append( filter.value )
		if not model.filter_order.count( filter.value ):
			print
			print filter.value
			print 'Please choose from the provided filter list.'
			sys.exit()
else:
	filters.append( form['filters'].value )
	if not model.filter_order.count( form['filters'].value ):
		print
		print 'Please choose from the provided filter list.'
		sys.exit()

# get list of redshifts to calculate values at
zs = []
custom_zs = True
if 'zs' in form and form['zs'].value:
	# get z values from user's list and make sure they are all numbers
	for z_s in form['zs'].value.split():
		try:
			z = float(z_s)
		except ValueError, TypeError:
			continue
		else:
			zs.append( z )
if len( zs ) == 0:
	zs = model.get_zs( zf - 0.1 )
	custom_zs = False
nzs = len( zs )

# set ab or vega output
mags = "AB"
vega = False
if form['output'].value == 'vega':
	mags = "Vega"
	vega = True

# set normalization
if "norm_z" in form and "norm" in form and "norm_filter" in form and "frame" in form and "norm_type" in form:
	if not model.filter_order.count( form['norm_filter'].value ):
		print
		print 'The requested normalization filter does not exist!'
		sys.exit()
	vega_norm = False if form['norm_type'].value == "ab" else True
	apparent = False if form['frame'].value == "absolute" else True
	model.set_normalization( form['norm_filter'].value, float( form['norm_z'].value ), float( form['norm'].value ), vega=vega_norm, apparent=apparent )

# get the normalization
norm = model.get_normalization( zf )
mult_norm = model.get_normalization( zf, flux=True )

# set the output filename
filename = form['filename'].value if "filename" in form else 'zf_%s' % form['zf'].value
if form['output_type'].value != 'to_browser': print 'Content-Disposition: attachment; filename="%s"' % filename
print

# generate a nice looking header
print "# Original Filename:   %s" % model.filename
print "# zf:                  %s" % form['zf'].value
print "# SFH:                 %s" % form['sfh'].value
if form['sfh'].value == 'Burst':
	print "# Burst Duration:      %s" % tau_val
elif form['sfh'].value != 'SSP':
	print "# Tau:                 %s" % tau_val
print "# Metallicity (z):     %s" % form['met'].value
print "# IMF:                 %s" % imf_val
print "# Cosmology:           Om=%.4f Ol=%.4f h=%.4f w=%.4f" % (model.cosmo.Om,model.cosmo.Ol,model.cosmo.h,model.cosmo.w)
print "# Magnitude System:    %s" % mags
if norm != 0:
	m = 'm' if model.norm['apparent'] else 'M'
	type = 'Vega' if model.norm['vega'] else 'AB'
	print "# Normalization        %s(%s) = %s %s mags @ z = %s" % (m,model.norm['filter'],form['norm'].value,type,form['norm_z'].value)
print "#"
print "# Column Descriptions:"

# column formats
col_formats = { 'abs_mags': '%8.4f', 'app_mags': '%8.4f', 'obs_mags': '%8.4f', 'kcors': '%8.4f', 'ecors': '%8.4f', 'ekcors': '%8.4f', 'rest_ml_ratios': '%7.4f', 'obs_ml_ratios': '%7.4f', 'solar_rest_mags': '%7.4f', 'solar_obs_mags': '%7.4f' }
# and headers
col_headers = { 'abs_mags': "# %s %s rest-frame absolute magnitude", 'obs_mags': "# %s %s observed-frame absolute magnitude", 'app_mags': "# %s %s apparent mangnitude", 'kcors': "# %s %s k-correction", 'ecors': "# %s %s e-correction", 'ekcors': "# %s %s e+k-correction", 'rest_ml_ratios': "# %s %s rest-frame mass-to-light ratios", 'obs_ml_ratios': "# %s %s observed-frame mass-to-light ratios", 'solar_rest_mags': "# %s %s solar rest-frame absolute magnitude", 'solar_obs_mags': "# %s %s solar observed-frame absolute magnitude" }

# figure out what filter columns to use
cols = []
if 'abs_mags' in form: cols.append( 'abs_mags' )
if 'obs_mags' in form: cols.append( 'obs_mags' )
if 'app_mags' in form: cols.append( 'app_mags' )
if 'kcors' in form: cols.append( 'kcors' )
if 'ecors' in form: cols.append( 'ecors' )
if 'ekcors' in form: cols.append( 'ekcors' )
if 'rest_ml_ratios' in form: cols.append( 'rest_ml_ratios' )
if 'obs_ml_ratios' in form: cols.append( 'obs_ml_ratios' )
if 'solar_rest_mags' in form: cols.append( 'solar_rest_mags' )
if 'solar_obs_mags' in form: cols.append( 'solar_obs_mags' )
ncols = len( cols )

# distance moduli, ages, and masses aren't repeated for each filter, so they are extra columns
extra_cols = 0
if 'dmods' in form: extra_cols += 1
if 'ages' in form: extra_cols += 1
if 'masses' in form: extra_cols += 1

# what is the format for column numbering in header?  Based on total number of columns
format = '%%%dd' % int( np.log10( len( filters )*ncols + 1 + extra_cols )+1 )
print "# %s redshift" % (format % 1)

# headers and columns for distance moduli, ages, and masses
ages_col = 1
masses_col = 1
if 'dmods' in form:
	print "# %s distance modulus" % (format % 2)
	ages_col += 1
	masses_col += 1
if 'ages' in form:
	masses_col += 1
	print "# %s age (gyrs)" % (format % (ages_col+1))
if 'masses' in form:
	print "# %s mass (solar masses)" % (format % (masses_col+1))

# now labels for the filter columns
# also build formats while we're at it
formats = ['%8.5f'] if custom_zs else ['%6.3f']
if 'dmods' in form: formats.append( '%7.4f' )
if 'ages' in form: formats.append( '%9.6f' )
if 'masses' in form: formats.append( '%11.5e' )
c = 2 + extra_cols
for filter in filters:
	for col in cols:
		print col_headers[col] % (format % c, filter)
		formats.append( col_formats[col] )
		c += 1

# now prepare data array
data = np.empty( (nzs,len( filters )*ncols+1+extra_cols) )
# store redshifts
data[:,0] = zs
# distance moduli (if requested)
if 'dmods' in form: data[:,1] = model.get_distance_moduli( zf, zs=zs, nfilters=1 )
# ages (if requested)
if 'ages' in form: data[:,ages_col] = model.get_age( zf, zs, units='gyrs' )
# and masses (if requested)
if 'masses' in form: data[:,masses_col] = model.get_masses( zf, zs, nfilters=1 )*mult_norm

# now loop through the filters and fill up the data array
c = 1 + extra_cols
for (i,filter) in enumerate(filters):

	for col in cols:

		# fetch appropriate column
		if col == 'abs_mags':
			mags = model.get_absolute_mags( zf, filters=filter, zs=zs, vega=vega )
		elif col == 'obs_mags':
			mags = model.get_absolute_mags( zf, filters=filter, zs=zs, vega=vega ) + model.get_kcorrects( zf, filters=filter, zs=zs )
		elif col == 'app_mags':
			mags = model.get_apparent_mags( zf, filters=filter, zs=zs, vega=vega )
		elif col == 'kcors':
			mags = model.get_kcorrects( zf, filters=filter, zs=zs )
		elif col == 'ecors':
			mags = model.get_ecorrects( zf, filters=filter, zs=zs )
		elif col == 'ekcors':
			mags = model.get_ekcorrects( zf, filters=filter, zs=zs )
		elif col == 'rest_ml_ratios':
			mags = model.get_rest_ml_ratios( zf, filters=filter, zs=zs )
		elif col == 'obs_ml_ratios':
			mags = model.get_observed_ml_ratios( zf, filters=filter, zs=zs )
		elif col == 'solar_rest_mags':
			mags = model.get_solar_rest_mags( filters=filter, nzs=nzs, vega=vega )
		elif col == 'solar_obs_mags':
			mags = model.get_solar_observed_mags( zf, filters=filter, zs=zs, vega=vega )

		# add to data array
		data[:,c] = mags

		c += 1

# now loop through the data array and write out data
for i in range( nzs ):
	print ' '.join([format % val for format,val in zip(formats, data[i,:])])

# finally, store requested model in database

# make a dictionary with field/values for the table....
mysql_data = {	'time':			'%d' % time.time(),
		'zf':			"'%s'" % zf,
		'model':		"'%s'" % form['model'].value.lower(),
		'met':			"'%s'" % form['met'].value,
		'imf':			"'%s'" % imf_val,
		'sfh':			"'%s'" % form['sfh'].value,
		'tau':			"'%s'" % tau_val,
		'filters':		"'%s'" % ', '.join( filters ) }

mysql_data['output'] = "'vega'" if vega else "'ab'"
mysql_data['dmods'] = '1' if 'dmods' in form else '0'
mysql_data['ages'] = '1' if 'ages' in form else '0'
mysql_data['masses'] = '1' if 'masses' in form else '0'
mysql_data['abs_mags'] = '1' if 'abs_mags' in form else '0'
mysql_data['obs_mags'] = '1' if 'obs_mags' in form else '0'
mysql_data['app_mags'] = '1' if 'app_mags' in form else '0'
mysql_data['kcors'] = '1' if 'kcors' in form else '0'
mysql_data['ecors'] = '1' if 'ecors' in form else '0'
mysql_data['ekcors'] = '1' if 'ekcors' in form else '0'
mysql_data['rest_ml_ratios'] = '1' if 'rest_ml_ratios' in form else '0'
mysql_data['obs_ml_ratios'] = '1' if 'obs_ml_ratios' in form else '0'
mysql_data['solar_rest_mags'] = '1' if 'solar_rest_mags' in form else '0'
mysql_data['solar_obs_mags'] = '1' if 'solar_obs_mags' in form else '0'

if model.get_normalization( zf ) != 0:
	mysql_data['norm'] = "'%f'" % model.norm['norm']
	mysql_data['norm_z'] = "'%f'" % model.norm['z']
	mysql_data['norm_filter'] = "'%s'" % model.norm['filter']
	mysql_data['frame'] = "'observed'" if model.norm['apparent'] else "'absolute'"
	mysql_data['norm_type'] = "'vega'" if model.norm['vega'] else "'ab'"

# build sql query
fields = []
values = []
for (field,value) in mysql_data.iteritems():
	fields.append( field )
	values.append( value )

query = "INSERT INTO ezgal_runs (%s) VALUES (%s)" % (', '.join( fields ),', '.join( values ))

# connect to the database
db = _mysql.connect( "mysql.baryons.org", "ufbaryons", "AsTROsq1", "baryons_main" )

# and insert
db.query( query )