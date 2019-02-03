import json
from google.cloud import pubsub_v1




def onDroneEventHttp(request):
    droneEvent = request.get_json()
    print ("receiving:{}".format(droneEvent))
    command = {}

    if (droneEvent['event'] == 'WAITING_FOR_COMMAND'):
        command = onWaitingForCommandEvent(droneEvent)

    if (droneEvent['event'] == 'PARCEL_DELIVERED'):
        command = onParcelDeliveredEvent(droneEvent)

    if (droneEvent['event'] == 'PARCEL_GRABBED'):
        command = onParcelGrabbedEvent(droneEvent)

    if (droneEvent['event'] == 'DESTINATION_REACHED'):
        command = onDestinationReachedEvent(droneEvent)

    if (droneEvent['event'] == 'MOVING'):
        command = onMovingEvent(droneEvent)

    if command:
        publish_messages(json.dumps(command))

    return "Ok"


def onWaitingForCommandEvent(droneEvent):
    todo = {}
    todo = todo["teamId"] = droneEvent['teamId']
    todo["command"] = {'name': 'MOVE', 'location': {}}
command: {
    name: 'MOVE',
    location: {
        latitude: x,
        longitude: y
    },
    return todo


def onParcelDeliveredEvent(droneEvent):
    return None


def onParcelGrabbedEvent(droneEvent):
    return None


def onDestinationReachedEvent(droneEvent):
    return None


def onMovingEvent(droneEvent):
    return None


def publish_messages(message):
    publisher = pubsub_v1.PublisherClient()

    topic_path = publisher.topic_path("jbc-atl-sal-func-techevent", "drone-command")

    data = message.encode('utf-8')

    future = publisher.publish(topic_path, data=data)
    print ('Published {} of message ID {}.'.format(data, future.result()))
