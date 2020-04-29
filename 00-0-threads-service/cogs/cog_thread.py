#!/usr/bin/python3

import queue
import threading
import time

from playLib.th_thread import th_threads
from playLib.bo_bucket import bo_get_bucket_list


bucket_name = 'dev-et-data'
prefix='NDVI_filled/2001/'
lista=bo_get_bucket_list(bucket_name, prefix)
maxcnt = 20
cnt=0
bucket='dev-et-data'
work_list = []
for file_obj in lista:
    if file_obj.endswith('.tif'):
        cnt=cnt+1
        prefix = '/'.join(file_obj.split('/')[0:-1])
        filen = file_obj.split('/')[-1]
        argv = '/'.join([bucket,prefix,filen])
        cmd = 'cogxfer.py ' + argv
        msg = str(cnt)
        msg=cmd
        print(msg)
        if (cnt < maxcnt):
            work_list.append(msg)

#work_list = ["One", "Two", "Three", "Four", "Five"] +  ["One", "Two", "Three", "Four", "Five"]
thread_count = 5

my_threads = th_threads(thread_count)

print(work_list)

my_threads.fill_q(work_list)


# wait for join

my_threads.join()
