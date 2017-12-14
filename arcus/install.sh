#!/bin/bash
apt install sshpass -y

cd /opt/arcus/scripts/

REPLACE=${MEMCACHED//;/:2181,}
REPLACE=${REPLACE: :-1}
sed -i 's/127.0.0.1:2181/'"${REPLACE}"'/g' ./arcus.sh

SETTING=""
export IFS=";"
for server in $MEMCACHED;
do
    sshpass -p "memcached" scp -o StrictHostKeyChecking=no /root/.ssh/authorized_keys $server:/root/.ssh/
    SETTING=$SETTING"{\"hostname\":\"$server\",\"ip\":\"$server\",\"config\":{\"port\":\"11211\"}},{\"hostname\":\"$server\",\"ip\":\"$server\",\"config\":{\"port\":\"11212\"}},"
done

echo "{\"serviceCode\": \"ite3068-cloud\",\"servers\":[${SETTING: :-1}],\"config\":{\"threads\":\"6\",\"memlimit\":\"100\",\"connections\":\"1000\"}}" > "conf/ite3068.json"

./arcus.sh deploy ./conf/ite3068.json
./arcus.sh zookeeper init
./arcus.sh zookeeper start
./arcus.sh memcached register conf/ite3068.json

# ./arcus.sh quicksetup conf/ite3068.json
./arcus.sh memcached start ite3068-cloud
