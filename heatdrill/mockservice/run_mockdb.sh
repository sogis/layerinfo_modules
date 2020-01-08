#!/bin/bash

echo "=========================================================="
echo "Docker container for test PostgreSQL database with postgis"
echo "Uses the following Docker image:"
echo "https://hub.docker.com/r/mdillon/postgis"
echo "=========================================================="

if [ "$1" == "bg" ] #bg - background
  then
    PARA="-d"
  else
    PARA=""
fi

docker run $PARA  \
  --name heatdrill_mockdb \
	-e POSTGRES_PASSWORD=postgres \
    -p 5432:5432 \
    --rm \
    sogis/heatdrill_mockdb


#Connect to db with username postgres (default) and password postgres (password is set by POSTGRES_PASSWORD)
