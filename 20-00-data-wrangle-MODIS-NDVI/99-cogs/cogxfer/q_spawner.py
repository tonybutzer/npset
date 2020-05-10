"""Now Consume those Right here"""
import os
import time
from playLib.wq_que import wq_listener

from playLib.log_logger import log_make_logger

global log
log=log_make_logger('Q_SPAWNER')


wq_listener()

