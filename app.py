import argparse
import json
import pickle
from subprocess import Popen, PIPE

project = "ite3068"

parser = argparse.ArgumentParser(description='ITE3068 Project manager application', prog="ITE3068 Project manager")
parser.add_argument('action', choices=('start', 'stop'))
parser.add_argument('--setting', nargs='?', type=str, default='settings.json')

args = parser.parse_args()

setting = json.load(open(args.setting))

def execute(commands):
    process = Popen(commands.split(' '), stdout=PIPE, stderr=PIPE)
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
    network = execute("docker network create {}".format(project))
    containers = [execute(docker_run(container)) for container in setting]
    print ('network: ', network, 'started')
    list(map(print, containers))
    if all(container for container in containers):
        pickle.dump(containers, open('containers.p', 'wb'))
        print ('All container started!')
    else:
        print ('Error raised while starting')

    # volumn
    for container in setting:
        for volumn in container.get('volumn', list()):
            tar, obj = volumn.split(':')
            execute("docker cp {} {}:{}".format(tar, container['name'], obj))

    # run command
    for container in setting:
        for cmd in container.get('command', list()):
            print ("{} run command: {}".format(container['name'], cmd))
            execute("docker exec {} {}".format(container['name'], cmd))

elif args.action == 'stop':
    containers = pickle.load(open('containers.p', 'rb'))
    results = [execute(docker_stop(container)) for container in containers]
    list(map(print, results))
    network = execute("docker network rm {}".format(project))
    print ('network: ', network, 'started')
    if all(result for result in results):
        print ('All container stopped!') 
    else:
        print ('Error raised while stoping')
