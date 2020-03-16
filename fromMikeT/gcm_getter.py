import urllib,os
import urllib.request

#example_filename = 'macav2metdata_tasmax_CanESM2_r1i1p1_rcp85_2091_2095_CONUS_daily.nc'
params_to_get = ["tasmax","tasmin","_pr_"]
#params_to_get = ["tasmax"]

catalog_url = 'http://thredds.northwestknowledge.net:8080/thredds/catalog/MACAV2/CSIRO-Mk3-6-0/catalog.html'
the_catalog = urllib.request.urlretrieve(catalog_url,'catalog.html')
download_base_url = "http://thredds.northwestknowledge.net:8080/thredds/fileServer/MACAV2/CSIRO-Mk3-6-0/"

current_file_list = os.listdir('.')

i = 0
for param_to_get in params_to_get:
    infile = open('catalog.html','rt')
    for line in infile:
        if '<a href' not in line: continue
        if 'dataset' not in line: continue
        if param_to_get not in line: continue
        if 'daily' not in line: continue
        if 'historical' in line: continue
        first = line.split('/')[1]
        filename = first.split('>')[0]
        filename = filename[:-1]
        if filename in current_file_list: 
            print('Skipping: ', filename)
            continue
        download_url = download_base_url + filename
        print(download_url)
        urllib.request.urlretrieve(download_url, filename)
        i+=1
        #if i > 0 :break
    infile.close()
    


