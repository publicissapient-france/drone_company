#!/usr/bin/env bash
pip install -r requirements.txt
gcloud beta functions deploy onDroneEventHttp --runtime python37 --trigger-http --region=europe-west1