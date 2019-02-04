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

    response = analyseMessage(droneEvent)
    if response:
        publish_messages(json.dumps(response), topicName)


def analyseMessage(message):
    # write your code here
    command = {}
    if (message['event'] == 'WAITING_FOR_COMMAND'):
        command = onWaitingForCommandEvent(message)

    elif (message['event'] == 'MOVING'):
        command = onMovingEvent(message)

    elif (message['event'] == 'MOVE_LOCATION_ERROR'):
        command = onMoveLocationError(message)

    return command


def onWaitingForCommandEvent(droneEvent):

    parcels_ = droneEvent["droneInfo"]["parcels"]
    if len(parcels_) > 0:
        return {"teamId": droneEvent['teamId'],
                "command": {"name": "MOVE",
                            "location": parcels_[0]["location"]["delivery"],

                            },
                }
    else:
        return {"teamId": droneEvent['teamId'],
                "command": {"name": "MOVE",
                            "location": droneEvent["availableParcelsForTeam"][0]["location"]["pickup"],

                            },
                }


def onMovingEvent(droneEvent):
    # write your code here
    return None


def onMoveLocationError(droneEvent):
    # write your code here
    return None
