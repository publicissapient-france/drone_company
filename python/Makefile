
register:
	# To be register in the game
	curl -d '{"teamId":"YOUR TEAM ID HERE", "url":"YOUR CLOUD FUNCTION URL HERE"}'\
	 -H "Content-Type: application/json" -X POST https://europe-west1-jbc-atl-sal-func-techevent.cloudfunctions.net/droneCallBackSetter

install:
	# To install dependencies
	sudo pip install -r requirements.txt
	
deploy:
	# To deploy in App Engine
	gcloud beta functions deploy onDroneEventHttp --runtime python37 --trigger-http --region=europe-west1

test:
	#To run all the tests
	python3 -m unittest