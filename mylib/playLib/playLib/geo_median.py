import geopandas as gpd
import rasterio as rio
import os
from rasterio.windows import from_bounds
import numpy as np

def clip_by_geojson(infile,geojson_file, nan='zero'):

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

        if (nan == 'zero'):
            rst[(rst < 0)] = 0
        else:
            rst[(rst < 0)] = np.nan

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


import rasterio as rio
import xarray as xr

def xarray_from_list(file_list, time_list, observation):
    datasets=[]
    for i in range(0, len(file_list)):
        url = file_list[i]
        time_name = time_list[i]
        da = xr.open_rasterio(url)
        da = da.squeeze().drop(labels='band')
        coords = da.coords
        coords['time'] = time_name
        da.assign_coords(coords)
        ds = da.to_dataset(name=observation)
        datasets.append(ds)
    DS = xr.concat(datasets, join='override', dim='time')
    return DS

import numpy
def clipped_np3d_from_list(file_list, geojson_file, nan='zero'):
    nps=[]
    for i in range(0, len(file_list)):
        url = file_list[i]
        ary=clip_by_geojson(url,geojson_file, nan)
        nps.append(ary)
    #NPA= numpy.concatenate(nps,axis=0)
    NPA= numpy.dstack(tuple(nps))
    return NPA
