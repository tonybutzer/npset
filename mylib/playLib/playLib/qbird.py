"""
Module Documentation
Class Qbird

simple message queues with rabbitmq
"""

import pika


class Qbird(object):
    """
    Qbird is and object that manages rabbitmq queues

    Parameters:
        rabbit_host: the name of the host where rabbitmq lives - defaul 'localhost'
    """

    def __init__(self, rabbit_host, queue_name):
        """Return a Qbird object
        """
        connection = pika.BlockingConnection(pika.ConnectionParameters(rabbit_host,heartbeat=10000))
        self.connection=connection
        self.channel = connection.channel()
        self.channel.basic_qos(prefetch_count=1)
        self.queue = queue_name

    def q_declare(self):
        self.channel.queue_declare(queue=self.queue)

    def q_publish(self,msg):
        self.channel.basic_publish(exchange='',
                      routing_key=self.queue,
                      body=msg)

    """
    These are reciever routines
    """

    def q_set_callback(self, callback_routine):
        self.channel.basic_consume(queue=self.queue,
            on_message_callback=callback_routine)
            #,auto_ack=True,on_message_callback=callback_routine)

    def q_consume(self):
        self.channel.start_consuming()




