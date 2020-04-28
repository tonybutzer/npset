import time
import rediswq
import os

from playLib.log_logger import log_make_logger

global log
log=log_make_logger('WQ_DISPATCHER')


wq_listener():
    host="redis-service"

    q = rediswq.RedisWQ(name="job2", host="redis")
    log.info("Worker with sessionID: " +  q.sessionID())
    log.info("Initial queue state: empty=" + str(q.empty()))
    while not q.empty():
        item = q.lease(lease_secs=10, block=True, timeout=2)
        if item is not None:
            itemstr = item.decode("utf-8")
            print("Working on " + itemstr)
            time.sleep(10) # Put your actual work here instead of sleep.
            # later this will call wq_system
            q.complete(item)
        else:
            log.info("Waiting for work")
    log.info("Queue empty, exiting")


def wq_system(task):
    print("rq_dispatch the TASK is %s" % task)
    msg = 'I will spawn thee: ', task
    log.info(msg)
    cmd = 'python3 ./' + task
    log.info(cmd)
    os.system(cmd)

