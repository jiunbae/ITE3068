cd /opt

apt-get update && apt-get install -y python3-pip python-pip python3 python librrd-dev  libpython3-dev libpython-dev git net-tools

git clone https://github.com/naver/hubblemon.git

mv collect_client.client_mysql_plugin.py hubblemon/collect_client/client_mysql_plugin.py
mv collect_client.run_client.py hubblemon/collect_client/run_client.py
mv common.settings.py hubblemon/common/settings.py

cd /opt/hubblemon

pip3 install psutil rrdtool

pip3 install -r requirements.txt

nohup python3 collect_server/run_server.py &
sleep 1
nohup python3 collect_server/run_listener.py &
sleep 1
nohup python3 collect_client/run_client.py &
sleep 1

nohup python3 manage.py migrate &
sleep 1
nohup python3 manage.py runserver  0.0.0.0:$HUBBLEMON &
