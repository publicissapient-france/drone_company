import json
import logging

from pubsubUtils import publish_messages


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
        publish_messages(json.dumps(command))

    return "Ok"


#
def onWaitingForCommandEvent(droneEvent):
    response = {}
    response.
    response["teamId"] = droneEvent['teamId'],
    response["command"] = {},
    response["command"]["Name"]= "MOVE",
    return response


def onMovingEvent(droneEvent):
    # write your code here
    return None


def onMoveLocationError(droneEvent):
    # write your code here
    return None
