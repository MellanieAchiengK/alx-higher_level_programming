#!/usr/bi/env bash
#sends a DELETE request to the URL passed as the first argument
curl -s -X "$1" DELETE | echo "I'm a DELETE request"
