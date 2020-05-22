import geopandas as gpd
import rasterio as rio
import os
from rasterio.windows import from_bounds
#from rasterio.enums import Resampling

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


import matplotlib.pyplot as pyplot
from rasterio.plot import show

def my_plot(array):
    cmaps = ['Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r']
    axs=()
    fig, axs = pyplot.subplots(1,8, figsize=(21,21))
    for i in range(0,8):
        show(array, ax=axs[i], cmap=cmaps[i], title=cmaps[i])
    pyplot.show()



