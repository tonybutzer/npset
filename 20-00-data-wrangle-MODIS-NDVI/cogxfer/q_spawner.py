"""Now Consume those Right here"""
import os
import time
from playLib.rq_que import workerbee

from playLib.log_logger import log_make_logger

global log
log=log_make_logger('Q_SPAWNER')


redisURL = 'http://redis'
task='COGS'
workerbee(redisURL,task)

