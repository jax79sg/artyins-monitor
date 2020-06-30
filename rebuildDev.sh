#!/bin/bash
docker rmi -f artyins-monitor
mkdir -p dockerdev
sudo rm -r dockerdev/artyins-monitor
rsync -r ../artyins-monitor dockerdev/
docker build ./dockerdev/. --no-cache -t artyins-monitor
