
# Register your cloud function to the game engine
[Dashboard](https://deploy-techevent-drone.appspot.com/)
Run the following example command with your own values:

```
make register team="YOUR TEAM ID HERE" url="YOUR CLOUD FUNCTION URL HERE"
```

# Deploy your cloud function 

Run the following command:

```
make deploy
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
    "parcels": [ <-- List of parcels currently carried by your drone
        {
            "location": {
                "delivery": {
                    "latitude": 48.89913913916235,
                    "longitude": 2.4160708432981473
                },
                "pickup": {
                    "latitude": 48.90704487288879,
                    "longitude": 2.281904373627992
                }
            },
            "parcelId": "03fff885-...",
            "score": 50,
            "status": "GRABBED",
            "teamId": "all",
            "type": "CLASSIC"
        }
    ],
    "score": 0
  },
  "availableParcelsForTeam": [ <-- List of parcels available to pickup
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
      "teamId": "all",
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

*Note: you will only receive events from your drone*

# All Events 

"**event**" attribut is the type of event currently received.
"**event**" values can be one of the following:
- WAITING_FOR_COMMAND (the drone is waiting for a new command even if its operating)
- MOVING (the drone is currently moving to its move destination set in the command)
- MOVE_LOCATION_ERROR (if the move location you sent in command is not valid)

If your drone is currently flying to a point then you will receive at each tick an event "MOVING" until it reached its destination.
If your drone is not moving and so is waiting for a command you will receive a each tick an event "WAITING_FOR_COMMAND".

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
make install test
 ```
 *  If your not sure about js code you can have a nice sandbox at [repl.it](https://repl.it/languages)



# GamePlay
    Todo  
      

# Optimisation

Turfjs "Advanced geospatial analysis for browsers and Node.js"

[Calculates the distance between two points](http://turfjs.org/docs#distance)

