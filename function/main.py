
from google.cloud import pubsub_v1
import json

teamId="red-111"

def onDroneEventHttp(request):
	droneEvent =request.get_json()
	print ("receiving:{}".format(droneEvent))
	command = {}

	if (droneEvent and droneEvent['event'] == 'INIT'):
		command["teamId"] = droneEvent['teamId']
		command ["command"] = { 'name': 'READY', 'topicUrl' : droneEvent['topicUrl'] } 

	if  command :
		publish_messages(json.dumps(command))
	
	return "Ok"




def publish_messages(message):
	publisher = pubsub_v1.PublisherClient()

	topic_path = publisher.topic_path("jbc-atl-sal-func-techevent","drone-command")

	data = message.encode('utf-8')

	future = publisher.publish(topic_path, data=data)
	print ('Published {} of message ID {}.'.format(data, future.result()))

