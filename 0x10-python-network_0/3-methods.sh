#!/bin/bash

# Check if url exist or, is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

#  collect and store input from command line
URL="$1"

# Send an OPTIONS request to the URL and display the allowed methods
curl -s -X OPTIONS -i "$URL" | awk '/Allow:/ {print $2}'

