import json
import logging

from pubsubUtils import publish_messages

topicName = 'projects/jbc-atl-sal-func-techevent/topics/drone-command'


def onDroneEventHttp(request):
    droneEvent = request.get_json()
    logging.info("receiving:{}".format(droneEvent))

    if not droneEvent or 'event' not in droneEvent:
        logging.error('bad droneEvent received')
        exit(1)

    command = {}

    if (droneEvent['event'] == 'WAITING_FOR_COMMAND'):
        command = onWaitingForCommandEvent(droneEvent)

    elif (droneEvent['event'] == 'MOVING'):
        command = onMovingEvent(droneEvent)

    elif (droneEvent['event'] == 'MOVE_LOCATION_ERROR'):
        command = onMoveLocationError(droneEvent)

    if command:
        publish_messages(json.dumps(command), topicName)

    return "Ok"


#
def onWaitingForCommandEvent(droneEvent):
    response = {"teamId": droneEvent['teamId'],
                "command": {"name": "MOVE",
                            "location":
                                {
                                    "latitude": 3,
                                    "longitude": 5
                                }
                            },
                }
    return response


def onMovingEvent(droneEvent):
    # write your code here
    return None


def onMoveLocationError(droneEvent):
    # write your code here
    return None
