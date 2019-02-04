from unittest import TestCase

from index import onMovingEvent, onWaitingForCommandEvent

message = {
    "teamId": "black-543",
    "event": "xxxxx",
    "droneInfo": {
        "location": {
            "latitude": 48.86439099043799,
            "longitude": 2.3426746801338623
        },
        "topicUrl": "https://europe-west1-...",
        "parcels": [
            {
                "teamId": "black-543",
                "status": "AVAILABLE",
                "location": {
                    "pickup": {
                        "latitude": 48.90524759169551,
                        "longitude": 2.2657060097635626
                    },
                    "delivery": {
                        "latitude": 48.867271697034234,
                        "longitude": 2.273857921355812
                    }
                },
                "type": "CLASSIC",
                "score": 50
            },
        ],
        "score": 0
    },
    "availableParcelsForTeam": [
        {
            "teamId": "black-543",
            "status": "AVAILABLE",
            "location": {
                "pickup": {
                    "latitude": 48.90524759169551,
                    "longitude": 2.2657060097635626
                },
                "delivery": {
                    "latitude": 48.867271697034234,
                    "longitude": 2.273857921355812
                }
            },
            "type": "CLASSIC",
            "score": 50
        },
        {
            "teamId": "black-543",
            "status": "AVAILABLE",
            "location": {
                "pickup": {
                    "latitude": 48.90524759169551,
                    "longitude": 2.2657060097635626
                }
            },
            "type": "SPEED_BOOST",
            "score": 0.1
        }
    ]
};


class TestMoving(TestCase):

    def test_receivingWAITINGFORCOMMAND(self):
        # Given
        localMessage = message
        localMessage["event"] = "WAITING_FOR_COMMAND"

        # When
        result = onWaitingForCommandEvent(localMessage)

        # Then
        self.assertEqual("black-543", result["teamId"])
        self.assertEqual("MOVE", result["command"]["name"])
        self.assertEqual(3, result["command"]["location"]["latitude"])
        self.assertEqual(5, result["command"]["location"]["longitude"])

    def test_receivingMOVING(self):
        # Given
        localMessage = message
        localMessage["event"] = "MOVING"

        # When
        result = onMovingEvent(localMessage)

        # Then
        self.assertEqual(None, result)
