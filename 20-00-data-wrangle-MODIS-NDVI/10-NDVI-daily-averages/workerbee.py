import os
import sys
import pickle
import geopandas as gpd
import rasterio as rio
from rasterio.windows import from_bounds
from playLib.log_logger import log_make_logger
from playLib.bo_bucket import s3cp



print(sys.argv[1])

my_work = int(sys.argv[1])

def clip_by_geojson(infile,outfile,geojson_file):

    filepath=infile
    geoms = gpd.read_file(geojson_file)
    print(geoms)
    left = geoms.bounds.minx[0]
    right = geoms.bounds.maxx[0]
    top = geoms.bounds.maxy[0]
    bottom = geoms.bounds.miny[0]

    print(left,right,top,bottom)

    with rio.open(filepath) as src:
        my_window = from_bounds(left, bottom, right, top, src.transform)
        print(my_window)

        rst = src.read(1, window=my_window)

        py, px = src.index(left, top)
        print('Pixel Y, X coords: {}, {}'.format(py, px))

        py, px = src.index(-90, 49.98)
        print('Pixel Y, X coords: {}, {}'.format(py, px))
        rst[(rst < 0)] = 0

        # You can then write out a new file
        meta = src.meta
        print(meta)
        #meta['width'], meta['height'] = rst.shape[1],rst.shape[0]
        meta['width'], meta['height'] = rst.shape[0],rst.shape[1]

        meta['transform'] = rio.windows.transform(my_window, src.transform)
        print(meta)

        with rio.open(outfile, 'w', **meta) as dst:
            dst.write(rst, 1)

        return rst


log=log_make_logger('WORKERBEE')
log.info('starting whatever YAY!')

newitems = pickle.load( open( "workitems_save.p", "rb" ) )

idx = my_work - 1
infile = newitems[idx]['infile']
temp = newitems[idx]['tempfile']
out = newitems[idx]['outfile']
geoj = newitems[idx]['geojson_file']

print(infile)
log.info(temp)
log.info(out)
log.info(geoj)
clip_by_geojson(infile,temp,geoj)

s3cp(temp,out)
os.remove(temp)
print("{} File Removed!".format(temp))
