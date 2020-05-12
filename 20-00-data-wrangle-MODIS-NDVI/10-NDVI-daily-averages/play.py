#!/usr/bin/env python

from playLib.th_thread import th_threads

work_list=[]
num_days = 366
for i in range(1,num_days+1):
    print(i)
    cmd = 'workerbee.py ' + str(i)
    work_list.append(cmd)
    

thread_count=64


my_threads = th_threads(thread_count)

print(work_list)

my_threads.fill_q(work_list)


my_threads.join()

