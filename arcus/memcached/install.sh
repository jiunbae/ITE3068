#!/bin/bash

cd /opt

tar -xzf arcus.tar.gz

mkdir -p data
echo $MEMCACHED_ID > data/myid

cp zoo.cfg arcus/zookeeper/conf/zoo.cfg

cd arcus/zookeeper

./bin/zkServer.sh start
