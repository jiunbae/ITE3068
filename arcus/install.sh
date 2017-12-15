#!/bin/bash
apt install sshpass -y

cd /opt/arcus/scripts/

CONF="conf/ite3068.json"

ADDRS=""
export IFS=";"
for server in $MEMCACHED;
do
    IP=`getent hosts $server | awk '{print $1 }'`
    ADDRS="$ADDRS$IP,"
done

REPLACE=${ADDRS//,/:2181,}
REPLACE=${REPLACE: :-1}

sed -i 's/127.0.0.1:2181/'"${REPLACE}"'/g' ./arcus.sh

SETTING=""
export IFS=","
for server in $ADDRS;
do
    sshpass -p "memcached" scp -o StrictHostKeyChecking=no /root/.ssh/authorized_keys $server:/root/.ssh/
    SETTING=$SETTING"{\"hostname\":\"$server\",\"ip\":\"$server\",\"config\":{\"port\":\"11211\"}},{\"hostname\":\"$server\",\"ip\":\"$server\",\"config\":{\"port\":\"11212\"}},"
done

echo "{\"serviceCode\": \"ite3068-cloud\",\"servers\":[${SETTING: :-1}],\"config\":{\"threads\":\"6\",\"memlimit\":\"100\",\"connections\":\"1000\"}}" > $CONF

sed -i 's/memcached -E/memcached -u memcached -E/g' arcus.sh
sed -i 's/memcached -E/memcached -u memcached -E/g' etc/arcus.sh
sed -i 's/memcached -E/memcached -u memcached -E/g' fabfile.py

./arcus.sh quicksetup $CONF
