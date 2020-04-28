import os

from redis import Redis
from rq import SimpleWorker, Queue

from playLib.log_logger import log_make_logger

global log
log=log_make_logger('RQ_DISPATCHER')


def rq_dispatch(task):
    print("rq_dispatch the TASK is %s" % task)
    msg = 'I will spawn thee: ', task
    log.info(msg)
    cmd = 'python3 ./' + task
    log.info(cmd)
    os.system(cmd)


def bullshit():
    print("BULSHIT Walks!")

def workerbee(redisServer, task):
    print("the TASK is %s" % task)

    queue = Queue(connection=Redis.from_url(redisServer))
    worker = SimpleWorker([queue], connection=queue.connection)
    worker.work()
