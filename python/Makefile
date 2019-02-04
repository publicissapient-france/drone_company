
register:
	# To be register in the game
	curl -d '{"teamId":$(team), "url":$url}'\
	 -H "Content-Type: application/json" -X POST https://europe-west1-jbc-atl-sal-func-techevent.cloudfunctions.net/droneCallBackSetter

install:
	# To install dependencies
	pip install -r requirements.txt
	
deploy:
	# To deploy in App Engine
	gcloud beta functions deploy $(name) --entry-point onDroneEventHttp --runtime python37 --trigger-http --region=europe-west1

test:
	#To run all the tests
	python -m un