#!/bin/bash
# Bash script that takes in a URL, sends a GET request to the URL, and displays the body of 200 status code response
curl -sL "$1"
