from playLib.bo_bucket import bo_get_bucket_list
from playLib.cl_numpy import np_load_cloud
from playLib.pl_objects import Play


def normal(x, amin, amax):
    x = (x+amin)/(amax-amin)
    return x

def main_stuff():
    
    bucket_name = "ga-et-data"
    prefix      = "Cloud_Veg_ET/Data/ETO/"
    list = bo_get_bucket_list(bucket_name, prefix)
    
    #print(list)
    
    pl=Play()
    cnt = 0
    for key in list:
        if 'npy' in key:
            cnt = cnt + 1
            #print(key)
            bucket_file = '{}/{}'.format(bucket_name, key)
            print(bucket_file)
            ary = np_load_cloud(bucket_file)
            amin = ary.min()
            amax = ary.max()
            print(amin, amax)
            ary = normal(ary, amin, amax)
            fname='/home/ubuntu/junkbox/a{0:03d}.png'.format(cnt)
            print(fname)
            pl.pl_create_png(fname, ary, cmap='Greens', title=fname, subtitle=fname)
            
            
    

main_stuff()