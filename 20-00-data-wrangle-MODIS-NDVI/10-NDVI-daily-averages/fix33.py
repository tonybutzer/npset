#!/usr/bin/env python

from playLib.th_thread import th_threads

work_list=[]
for i in range(33,33+1):
    print(i)
    cmd = 'workerbee.py ' + str(i)
    work_list.append(cmd)
    

thread_count=1


my_threads = th_threads(thread_count)

print(work_list)

my_threads.fill_q(work_list)


my_threads.join()

