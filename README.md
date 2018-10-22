# How to send a MOVE command to your drone


## Send the following command in the topic :

```
{
	teamId: 'your team id should be set here',
	command: {
	  name: 'MOVE',
	  location: {
	  	latitude: latitude where you want the drone to go,
	  	longitude: longitude where you want the drone to go
	  }
	}
}
```

# Event received by your Cloud Function

In the **availableParcelsForTeam** attribut you will get all the parcels that your drone can get.

**event** attribut is the type of event currently received.
**event** value can be :
- WAITING_FOR_COMMAND (the drone is waiting)
- MOVING
- DESTINATION_REACHED	
- PARCEL_GRABBED
- PARCEL_DELIVERED
- MOVE_LOCATION_ERROR (if the location you sent in command is outside the play ground)

At each tick (a tick = 1 second) you will receive an event.

So for example if your drone is currently flying to a point you will receive at each tick an event "MOVING"


## Example:

```
{
  "teamId": "black-543",
  "event": "WAITING_FOR_COMMAND",
  "droneInfo": {
    "location": {
      "latitude": 48.86439099043799,
      "longitude": 2.3426746801338623
    },
    "topicUrl": "https://europe-west1-...",
    "parcels": [],
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
}
```

# How to optimise your drone

## Turfjs "Advanced geospatial analysis for browsers and Node.js"

[Calculates the distance between two points](http://turfjs.org/docs#distance)

