#!/bin/bash

URL="$1"
EMAIL="test@gmail.com"
SUBJECT="I will always be here for PLD"

curl -s -X POST -d "email=$EMAIL&subject=$SUBJECT" "$URL"
