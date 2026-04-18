#!/bin/bash
# This script lists HTTP methods allowed by server
curl -sI -X OPTIONS "$1" | awk '/Allow/ {print $2}'
