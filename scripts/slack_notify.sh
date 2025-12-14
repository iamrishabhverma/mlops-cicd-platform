#!/bin/bash
curl -X POST -H 'Content-type: application/json' --data '{"text":"ML Pipeline Notification"}' $SLACK_WEBHOOK_URL
