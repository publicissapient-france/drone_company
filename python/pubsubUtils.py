import logging

from google.cloud import pubsub_v1

publisher = pubsub_v1.PublisherClient()


def publish_messages(message, topicName):
    logging.info("will send to topic {} : {}".format (topicName, message))
    topic_path = publisher.topic_path(topicName, "drone-command")

    data = message.encode('utf-8')

    future = publisher.publish(topic_path, data=data)
    logging.info('Published of message ID {}.'.format(future.result()))
