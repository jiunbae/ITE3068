cd /opt

apt-get update && apt-get install -y python3-pip python-pip python3 python librrd-dev  libpython3-dev libpython-dev git net-tools

git clone https://github.com/naver/hubblemon.git

mv collect_client.client_mysql_plugin.py hubblemon/collect_client/client_mysql_plugin.py
mv collect_client.run_client.py hubblemon/collect_client/run_client.py
mv common.settings.py hubblemon/common/settings.py

cd /opt/hubblemon

pip3 install psutil rrdtool

pip3 install -r requirements.txt

python3 collect_server/run_server.py &
python3 collect_server/run_listener.py &
python3 collect_client/run_client.py &
python3 manage.py migrate

python3 manage.py runserver 0.0.0.0:$HUBBLEMON
