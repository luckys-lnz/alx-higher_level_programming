#!/bin/bash

# Check if URL is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# URL from the command line argument
URL="$1"

# Send request to the URL and get the size of the body in bytes
SIZE=$(curl -s -o /dev/null -w '%{size_download}' "$URL")

# Display the size
echo "$SIZE"

