teams=amber-53 black-171 blue-978 brown-254 cyan-647 green-947 grey-92 lemon-871 lime-312 magenta-791 \
marin-902 orange-655 pink-556 purple-923 red-844 rubi-920 teal-95 violet-951 white-950 yellow-380

register: required-team required-url
	# To be register in the game
	curl -d '{"teamId":"$(team)", "url":"$(url)"}'\
	 -H "Content-Type: application/json" -X POST https://europe-west1-jbc-atl-sal-func-techevent.cloudfunctions.net/droneCallBackSetter

install:
	# To install dependencies
	sudo pip3 install -r requirements.txt
	
deploy:
	# To deploy in cloud function
	gcloud beta functions deploy onDroneEventHttp \
	--runtime python37 --trigger-http --region=europe-west1

bulk_deploy:
	# To deploy 20 functions
	for team in $(teams); do \
		echo $$team;\
		gcloud beta functions deploy $$team --entry-point=onDroneEventHttp --project=$(project) --runtime python37 --trigger-http --region=europe-west1; \
	done

bulk_register:
	# To register 20 functions
	for team in $(teams); do \
		data="{\"teamId\":\"$$team\", \"url\":\"https://europe-west1-test-drone-company.cloudfunctions.net/$$team\"}"; \
		echo $$data; \
		curl -d "$$data" \
        		 -H "Content-Type: application/json" -X POST https://europe-west1-jbc-atl-sal-func-techevent.cloudfunctions.net/droneCallBackSetter; \
	 done
test:
	#To run all the tests
	python3 -m unittest


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