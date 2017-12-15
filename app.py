import argparse
import json
import pickle
from subprocess import Popen, PIPE
from urllib import request
from time import sleep

project = "ite3068"

parser = argparse.ArgumentParser(description='ITE3068 Project manager application', prog="ITE3068 Project manager")
parser.add_argument('action', choices=('start', 'stop'))
parser.add_argument('--setting', nargs='?', type=str, default='settings.json')

args = parser.parse_args()

setting = json.load(open(args.setting))

def execute(commands, wait=True):
    print ('\tExecute: {}'.format(commands))
    process = Popen(commands.split(' '), stdout=PIPE, stderr=PIPE)
    if wait:
        stdout, stderr = process.communicate()
        return False if stderr else stdout.decode('utf-8')[:-1]

def docker_stop(container):
    return 'docker rm -f {}'.format(container)

def docker_run(setting):
    command = 'docker run -d --net={}'.format(project)
    if 'name' in setting:
        command += ' --name={}'.format(setting['name'])
    for port in setting.get('ports', list()):
        command += ' -p {}:{}'.format(port['host'], port['cont'])
    for key, value in setting.get('env', dict()).items():
        command += ' --env {}={}'.format(key, value)
    command += ' {}'.format(setting.get('docker', ''))
    return command

if args.action == 'start':
    # network
    print ('Docker network initializing ...')
    network = execute("docker network create {}".format(project))

    # container
    print ('Docker container initializing ...')
    containers = [execute(docker_run(container)) for container in setting]
    print ('network: {}'.format(network))
    if all(container for container in containers):
        pickle.dump(containers, open('containers.p', 'wb'))
        print ('All container started!')
    else:
        print ('Error raised while starting')

    # volumn
    print ('Docker volumn initializing ...')
    for container in setting:
        for volumn in container.get('volumn', list()):
            tar, obj = volumn.split(':')
            execute("docker cp {} {}:{}".format(tar, container['name'], obj))

    # run command
    print ('Docker commands executing ...')
    for container in setting:
        for cmd in container.get('commands', list()):
            execute("docker exec {} {}".format(container['name'], cmd), False)

    print ('Docker started!')

    # wait
    print ('Waiting for instance initializing ...')
    for container in setting:
        for k, v in container.get('wait', dict()).items():
            print ('{} Waiting {} ...'.format(container['name'], k))
            while True:
                try:
                    request.urlopen('http://{}/'.format(v))
                    break;
                except:
                    sleep(5)

    print ('Waiting done! Instance initialized!')

    ## Case for my app
    # nbase arc setup
    execute('docker exec nbase-arc /bin/bash -c /root/install.sh', False)

    # api server
    execute('python3 api/app.py', False)
    print ('API Server started!')

elif args.action == 'stop':
    # container
    print ('Docker container removing ...')
    containers = pickle.load(open('containers.p', 'rb'))
    results = [execute(docker_stop(container)) for container in containers]

    # network
    print ('Docker network removing ...')
    network = execute("docker network rm {}".format(project))
    print ('network: ', network, 'started')
    if all(result for result in results):
        print ('All container stopped!') 
    else:
        print ('Error raised while stoping')
