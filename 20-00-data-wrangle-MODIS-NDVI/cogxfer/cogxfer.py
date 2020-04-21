import os

from breed import Breed
from playLib.bo_bucket import bo_get_bucket_list

print("hello from Tony cogxfer")
print("hello AGAIN from Tony cogxfer")

breed = Breed()

print(breed.in_bucket)
print(breed.out_bucket)
print(breed.in_prefix)


list = bo_get_bucket_list(breed.in_bucket, breed.in_prefix)

tif_list = []
for item in list:
    if item.endswith('.tif'):
        # print(item)
        tif_list.append(item)

print("---"*25)
print(tif_list[0])

bucket_file = breed.in_bucket + '/' + tif_list[0]
cmd = 'aws s3 ls {}'.format(bucket_file)

print("---"*25)
print(cmd)

os.system(cmd)
