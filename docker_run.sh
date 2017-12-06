#!/bin/bash

docker run -d --name="arcus-admin" -h "arcus" ruo91/arcus
docker run -d --name="arcus-REMOVED-CREDENTIAL-1" -p 11211:11211 -h "REMOVED-CREDENTIAL-1" ruo91/arcus:REMOVED-CREDENTIAL
docker run -d --name="arcus-REMOVED-CREDENTIAL-2" -h "REMOVED-CREDENTIAL-2" ruo91/arcus:REMOVED-CREDENTIAL
docker run -d --name="arcus-REMOVED-CREDENTIAL-3" -h "REMOVED-CREDENTIAL-3" ruo91/arcus:REMOVED-CREDENTIAL
docker run -d --name=mysql -p 3306:3306 --env MYSQL_ROOT_PASSWORD=REMOVED-CREDENTIAL --env MYSQL_USER=maybe --env MYSQL_PASSWORD=REMOVED-CREDENTIAL --env MYSQL_DATABASE=ite3068 mysql:latest
docker run -d --name=nbase-arc -p 6000:6000 hyeongseok05/nbase-arc
