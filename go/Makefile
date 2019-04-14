
register: required-team required-url
	# To be register in the game
	curl -d '{"teamId":"$(team)", "url":"$(url)"}'\
	 -H "Content-Type: application/json" -X POST https://europe-west1-jbc-atl-sal-func-techevent.cloudfunctions.net/droneCallBackSetter

install:
	# To install dependencies

	
deploy:
	# To deploy in cloud function
	gcloud beta functions deploy onDroneEventHttp \
	--runtime=go111 --trigger-http --region=europe-west1

test:
	#To run all the tests


required-team:
    # Function to control if the variable team is set
	$(if $(team),,exit 1)

required-url:
    # Function to control if the variable url is set
	$(if $(url),,exit 1)


help:
	@printf   "$$(cat Makefile | grep -e "#\|^\w*: \|\w*:$$"| grep -v 'printf' |sed 's/^\(.*:\)/\\033\[1m \1 \\033[0m/g')"

.DEFAULT_GOAL := help
.PHONY: help register install deploy test required-url required-team