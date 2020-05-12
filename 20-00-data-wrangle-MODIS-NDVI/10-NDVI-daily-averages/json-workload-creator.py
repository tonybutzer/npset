#!/usr/bin/env python
# coding: utf-8

import sys

year = sys.argv[1]

if '20' not in year:
    print("Usagei: program  needs year argument")
    sys.exit(1)


def make_dict(cnt,infile,outfile,tempfile,geojf):
    workitem = {
        'count': cnt,
        'infile': infile,
        'outfile': outfile,
        'tempfile': tempfile,
        'geojson_file': geojf
    }
    
    return workitem



workitems=[]
#year = '2002'
for i in range(1,366+1):
    print(i)
    inf = '/vsis3/dev-et-data/compressed/NDVI_filled/{1}/{2}{0:03}.250_m_NDVI.tif'.format(i,year,year)
    tmp = 'data/gl{0:03}.tif'.format(i)
    out = 's3://dev-et-data/t50n-90e/{1}/{2}_t50n_m90e{0:03}.tif'.format(i,year,year)
    geoj = 'great_lakes_edit.geojson'
    
    wi = make_dict(i,inf,out,tmp, geoj)
    print(wi)
    workitems.append(wi)


import pickle


pickle.dump(workitems, open( "workitems_save.p", "wb" ))









