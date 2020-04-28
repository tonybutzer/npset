import sys 
import numpy as np
import xarray as xr

from os import listdir
from os.path import isfile, join

arg_names = ['command', 'cmap', 'fname']
args = dict(zip(arg_names, sys.argv))

print(args)
print("hello from tony and the create_png_cmd app")

from playLib.pl_objects import Play

pl=Play()

mypath='/mnt/ga-et-data/Cloud_Veg_ET/Data/ETO'
fname = args['fname']

full_filename = mypath +'/' + fname

ary = np.load(full_filename)

ary = np.flip(ary, axis=0)

ary[(ary<0)]=0

amin = ary.min()
amax = ary.max()

print(amin, amax)
def normal(x):
    global amin
    global amax
    x = (x+amin)/(amax-amin)
    return x

ary = normal(ary)

print(ary.min(), ary.max())

cmap=args['cmap']
output_file_name = './data/' + fname
pl.pl_create_png(output_file_name, ary, cmap=cmap)
