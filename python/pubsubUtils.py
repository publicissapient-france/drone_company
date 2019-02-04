import logging

from google.cloud import pubsub_v1

publisher = pubsub_v1.PublisherClient()


def publish_messages(message):
    logging.info("will send to topic {} : {}".format(message))
    topic_path = publisher.topic_path("jbc-atl-sal-func-techevent", "drone-command")

    data = message.encode('utf-8')

    future = publisher.publish(topic_path, data)
    logging.info('Published of message ID {}.'.format(future.result()))
