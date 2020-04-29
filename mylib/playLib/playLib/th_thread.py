import os
import queue
import threading
import time

from playLib.log_logger import log_make_logger

global log
log=log_make_logger('TH_DISPATCHER')


class th_thread (threading.Thread):
    def __init__(self, threadID, name, q, qlock):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
        self.qlock = qlock
        self.exit_flag = 0


    def run(self):
        print ("Starting " + self.name)

        while not self.exit_flag:
            self.qlock.acquire()
            if not self.q.empty():
                work = self.q.get()
                self.qlock.release()
                print ("%s processing %s" % (self.name, work))
                self._execute_work(work)
            else:
                self.qlock.release()
                time.sleep(1)

        print ("Exiting " + self.name)


    def exit_ok(self):
        self.exit_flag = 1

    def _execute_work(self, work):
        task = work
        print("th_dispatch the TASK is %s" % task)
        msg = 'I will spawn thee: ', task
        log.info(msg)
        cmd = 'python3 ./' + task
        log.info(cmd)
        os.system(cmd)



class th_threads():
    def __init__(self, thread_count):
        self.threads = []
        self.qlock = threading.Lock()
        self.q = queue.Queue(1000)
        for thread_id in range(thread_count):
            th_name = 'qworker_' + str(thread_id)
            thread = th_thread(thread_id, th_name, self.q, self.qlock)
            thread.start()
            self.threads.append(thread)
    def fill_q(self, work_list):
        self.qlock.acquire()
        for work in work_list:
            self.q.put(work)
        self.qlock.release()
    def join(self):
        # Wait for queue to empty
        while not self.q.empty():
            pass
        # Wait for all threads to complete
        for t in self.threads:
            # Notify threads it's time to exit
            t.exit_ok()
            t.join()
        print ("Exiting Main Thread")



