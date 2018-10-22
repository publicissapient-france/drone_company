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

# How to optimise your drone

## Turfjs "Advanced geospatial analysis for browsers and Node.js"

[Calculates the distance between two points](http://turfjs.org/docs#distance)

