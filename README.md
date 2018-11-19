# Get a google cloud project
[team sheet | https://docs.google.com/document/d/18iwSw9qpQ3DYrmVb-t5yWK5ILbmpe8NxfJAYLihFmi0/edit?ts=5bf2e940#heading=h.giqkauc06g0d]

# Register your cloud function to the game engine

Run the following example command with your own values:

```
curl -d '{"teamId":"YOUR TEAM ID HERE", "url":"YOUR CLOUD FUNCTION URL HERE"}' -H "Content-Type: application/json" -X POST https://europe-west1-jbc-atl-sal-func-techevent.cloudfunctions.net/droneCallBackSetter
```

# Move your drone

Type of command to send to move your drone :

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

# Event received 

Example of json that your cloud function will receive:

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
    "parcels": [], <-- List of parcels caring by your drone 
    "score": 0
  },
  "availableParcelsForTeam": [ <-- List of parcels to pickup
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
      "type": "SPEED_BOOST" <-- Pay attention this parcel is available for every teams. So check if it'is still vacant
      "score": 0.1
    }    
  ]
}
```

*Note: you will receive events only from your drone*

# All Events 
Because of at each tick is 1 second, your function could missed these events. 
So you should analyse first the situation and then acting one event.

**event** attribut is the type of event currently received.
**event** value can be :
- WAITING_FOR_COMMAND (the drone is waiting for a new command even if its operating)
- MOVING (the drone is currently moving to its move destination set in the command)
- MOVE_LOCATION_ERROR (if the move location you sent in command is not valid)

So for example if your drone is currently flying to a point you will receive at each tick an event "MOVING"

# Managing parcels

**droneInfo.parcels** attribut contains parcels that you have already grabbed and that you should deliver.

**availableParcelsForTeam** attribut you will get all the parcels that your drone can get.
There is currently two type parcel:

**"type": "CLASSIC"**
Typical parcel when the drone grab one of those he will have to go to the destination to earn the point.

**"type": "SPEED_BOOST"**
This one is special it will allow your drone to go faster !
For this one you don't need to deliver it.


# Must know
 *  In order to run tests 
 ``` 
 npn test
 ```
 *  If your not sure about js code you can have a nice sandbox at [repl.it](https://repl.it/languages)


# Optimisation

Turfjs "Advanced geospatial analysis for browsers and Node.js"

[Calculates the distance between two points](http://turfjs.org/docs#distance)

