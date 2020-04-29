import os
import sys

from breed import Breed
from playLib.bo_bucket import bo_get_bucket_list
from playLib.bo_bucket import s3cp
from playLib.log_logger import log_make_logger

def master_stuff():
    breed = Breed()

    log.info(breed.in_bucket)
    log.info(breed.out_bucket)
    log.info(breed.in_prefix)
    list = bo_get_bucket_list(bucket_name, prefix)

    tif_list = []
    for item in list:
        if item.endswith('.tif'):
            # print(item)
            tif_list.append(item)


def main_stuff(bucket_file, log):

    log.info("hello from Tony cogxfer")

    log.info(bucket_file)
    log.info("---"*25)

    breed = Breed()
    log.info(breed.out_bucket)


    just_file = bucket_file.split('/')[-1]
    local_file= 'junkbox/' + just_file
    cmd = 'rio --quiet cogeo create /vsis3/{} {}'.format(bucket_file, local_file)
    log.info("---"*25)
    log.info("---"*25)
    log.info(cmd)
    os.system(cmd)


    mid_prefix = '/'.join(bucket_file.split('/')[1:-1])
    out_prefix = breed.out_prefix + '/' + mid_prefix

    remote_file = 's3://' + breed.out_bucket + '/' + out_prefix + '/' + just_file
    log.info("---"*25)
    log.info("---"*25)
    log.info(local_file)
    log.info(remote_file)

    s3cp(local_file, remote_file)
    os.remove(local_file)

    xml_from_file = 's3://' + bucket_file + '.aux.xml'
    xml_to_file = remote_file + '.aux.xml'
    s3cp(xml_from_file, xml_to_file)
    log.info(xml_from_file)
    log.info(xml_to_file)

# end of main_stuff


# ----------------------------------------------

if len(sys.argv) > 1:
   global log
   log=log_make_logger('COG Compressor')
   log.info('starting cogification YAY!')
   bucket_file = sys.argv[1]

main_stuff(bucket_file, log)
