#!/bin/bash
# Bash script that takes in URL as argument, sends a GET request and displays the body of the response
curl -sH "X-School-User-Id: 98" "$1"
