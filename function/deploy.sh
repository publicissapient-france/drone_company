#!/usr/bin/env bash

gcloud beta functions deploy onDroneEventHttp --runtime=nodejs8 --trigger-http --region=europe-west1