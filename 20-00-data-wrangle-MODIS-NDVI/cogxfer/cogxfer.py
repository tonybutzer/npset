from breed import Breed
from playLib.bo_bucket import bo_get_bucket_list

print("hello from Tony cogxfer")
print("hello AGAIN from Tony cogxfer")

breed = Breed()

print(breed.in_bucket)
print(breed.out_bucket)
print(breed.in_prefix)


list = bo_get_bucket_list(breed.in_bucket, breed.in_prefix)

for item in list:
    if item.endswith('.tif'):
        print(item)
