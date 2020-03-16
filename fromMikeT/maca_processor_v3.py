import sys,os,datetime

def make_time_unlimited(fn, out_fn = 'nps_maca_time_unlimited.nc'):
    global input_path, output_path
    print('Making time dimension unlimited.')
    print(datetime.datetime.now())
    time_command = 'ncks --mk_rec_dmn time {i}{fn} -o {i}{out_fn}'.format(fn = fn, out_fn = out_fn, i = input_path)
    print(time_command)
    os.system(time_command)
    return out_fn
    
def convert_to_nc3(fn, out_fn = 'nps_maca_ready.nc'):
    global input_path, output_path
    print('Converting to nc3.')
    print(datetime.datetime.now())
    convert_command = 'nccopy -k classic {i}{fn} {i}{out_fn}'.format(fn = fn, out_fn = out_fn, i = input_path)
    print(convert_command)
    os.system(convert_command)
    os.remove(input_path + fn)
    return out_fn

def reproject(fn, out_fn = 'nps_maca_reprojected.tif'):
    global input_path, output_path
    print('Reprojecting.')
    print(datetime.datetime.now())
    #reproject_command = 'gdalwarp -t_srs "+proj=lcc +lat_1=25 +lat_2=60 +lat_0=42.5 +lon_0=-100 +x_0=0 +y_0=0 +datum=WGS84 +units=m +no_defs" -of netCDF -co "FORMAT=NC4" -multi {i}{fn} {i}{out_fn}'.format(fn = fn, out_fn = out_fn, i = input_path)
    reproject_command = 'gdalwarp -t_srs "+proj=lcc +lat_1=25 +lat_2=60 +lat_0=42.5 +lon_0=-100 +x_0=0 +y_0=0 +datum=WGS84 +units=m +no_defs" -multi -co "BIGTIFF=YES" {i}{fn} {i}{out_fn}'.format(fn = fn, out_fn = out_fn, i = input_path)
    print(reproject_command)
    os.system(reproject_command)
    os.remove(input_path + fn)
    return out_fn

def set_bounding_box(in_name, out_name): 
    global input_path, output_path
    print('Setting bounding box . . . ')
    print(datetime.datetime.now())
    out_name = out_name[:-4] + '_reprojected_with_extent'
    del_list = []
    the_nums = list(range(1,2000)) # This is more than needed. Extra commands above 1827 or so fail, but it solves the different number of days in hacky way.
    command1 = 'gdalwarp -s_srs "+proj=lcc +lat_1=25 +lat_2=60 +lat_0=42.5 +lon_0=-100 +x_0=0 +y_0=0 +datum=WGS84 +units=m +no_defs" -te -4560750.00000 -3090500.00000 3253250.00000 4984500.00000 -co "BIGTIFF=YES" {i}{in_name} {i}{out_name}{num2}.tif'
    
    for num in the_nums:
        pre_command = 'gdal_translate -b {num} {in_name} tempfoo.tif'.format(num = num, in_name = in_name)
        print(pre_command)
        os.system(pre_command)
        this_command = command1.format(in_name = 'tempfoo.tif' ,out_name = out_name, num2 = num, i = input_path)
        print(this_command)
        os.system(this_command)
        try:
            os.remove('tempfoo.tif')
            del_name = out_name + str(num)
            del_list.append(del_name)
        except:
            continue
    
    os.remove(input_path + in_name)
    return del_list, out_name

def resample(del_list):
    global input_path, output_path
    print('Resampling . . .')
    print(datetime.datetime.now())
    command2 = 'gdal_translate -outsize 7814 8075 -co "COMPRESS=DEFLATE" -co "BIGTIFF=YES" {i}{in_fn}.tif {o}{out_fn}'
    for fn in del_list:
        this_outname = fn + '_resampled.tif'
        this_command = command2.format(in_fn = fn, out_fn = this_outname, i = input_path, o = output_path)
        print(this_command)
        os.system(this_command)
        try:
            os.remove(input_path + fn + '.tif') 
        except:
            print('Failed to remove:', fn)
            continue
  
if __name__ == "__main__":
    web = True
    if web == False:
        input_path = './'
        output_path = './'
    else:
        input_path = './'
        output_path = '/home/ubuntu/results/'
        #output_path = './results/'
    start_name = 'copy1.nc'
    fl = os.listdir('.')
    done_list = os.listdir(output_path)
    done_numbers = [x.split('_')[0] for x in done_list]
    for start_name in fl:
        if start_name.split('.')[-1] != 'nc' : continue
        file_no = start_name.split('_')[0]
        if file_no in done_numbers:
            print('Skipping: ', start_name)
            continue
        print(start_name)
        ft_name = make_time_unlimited(start_name)
        converted_name = convert_to_nc3(ft_name)
        reprojected_name = reproject(converted_name)
        del_list, out_name = set_bounding_box(reprojected_name, start_name)
        resample(del_list)
    
