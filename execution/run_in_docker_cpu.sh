#!/bin/bash
# Change to the project root directory
cd "$(dirname "$(realpath "$0")")"
cd ..
# Generate a random name for the docker container
CONTAINERNAME=interactive_container_$RANDOM$RANDOM
# Start a docker container
docker run -d --name $CONTAINERNAME -i -v "$PWD":/project: -w /project tensorflow/tensorflow:latest sh
# Create a group that matches the current user's group, so that the useradd command will work correctly
docker exec $CONTAINERNAME groupadd --gid $(id -g) dockerusergroup
# Create a user that matches the current user, so if the user creates any files in the project directory, they can have correct permissions
docker exec $CONTAINERNAME useradd --system --create-home --home-dir /home/dockeruser --shell /bin/bash --gid $(id -g) --groups sudo --uid $(id -u) dockeruser
#  Update pip if needed
docker exec $CONTAINERNAME  pip3 install --upgrade pip
#  Download project dependencies
docker exec $CONTAINERNAME pip3 install --editable .
# Connect to the docker container interactively so the user can do what they want
docker exec -it -u $(id -u):$(id -g) $CONTAINERNAME /bin/bash
# Delete the docker container
docker kill $CONTAINERNAME
docker rm $CONTAINERNAME