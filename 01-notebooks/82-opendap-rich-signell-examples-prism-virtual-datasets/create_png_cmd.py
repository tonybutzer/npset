import sys 
arg_names = ['command', 'cmap', 'fname']
args = dict(zip(arg_names, sys.argv))

print(args)
print("hello from tony and the create_png_cmd app")

from playLib.pl_objects import Play

pl=Play()

import netCDF4
url = 'http://geoport-dev.whoi.edu/thredds/dodsC/prism4/monthly'

# create a dataset object
dataset = netCDF4.Dataset(url)

temp=dataset['temp_max'][1,:,:]

cmap=args['cmap']
fname = args['fname']
pl.pl_create_png(fname, temp, cmap=cmap)
