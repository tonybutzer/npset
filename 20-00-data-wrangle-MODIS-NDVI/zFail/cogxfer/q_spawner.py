"""Now Consume those Right here"""
import os
import time
from playLib.qbird import Qbird

from playLib.log_logger import log_make_logger

global log
log=log_make_logger('Q_SPAWNER')

def spawn_cmd(message):
    msg = 'I will spawn thee: ', message
    log.info(msg)
    cmd = 'python3 ./' + message
    log.info(cmd)
    os.system(cmd)

def callback(ch, method, properties, body):
    msg = body.decode('UTF-8')
    print(msg)
    log.info(msg)
    spawn_cmd(msg)

    ch.basic_ack(delivery_tag=method.delivery_tag)    


cnt=100;
while cnt>0:
    try:
        #qr=Qbird('localhost','tonyq')
        qr=Qbird('rabbitmq','tonyq')
    except:
        time.sleep(3)
        log.info('sleeping - waiting ... rabbitmq where are you?')
        continue
    break

qr.q_declare()

qr.q_set_callback(callback)

qr.q_consume()
