#!/usr/bin/python3

import queue
import threading
import time

from playLib.th_thread import th_threads


nameList = ["One", "Two", "Three", "Four", "Five"]

thread_count = 3

my_threads = th_threads(thread_count)

my_threads.fill_q(nameList)


# wait for join

my_threads.join()
