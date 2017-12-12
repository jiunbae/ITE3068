import argparse
import json
import pickle
from subprocess import Popen, PIPE

parser = argparse.ArgumentParser(description='ITE3068 Project manager application', prog="ITE3068 Project manager")
parser.add_argument('action', choices=('start', 'stop'))
parser.add_argument('--setting', nargs='?', type=str, default='settings.json')

args = parser.parse_args()

setting = json.load(open(args.setting))

def execute(commands):
    process = Popen(commands, stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    return False if stderr else stdout.decode('utf-8')[:-1]

def docker_stop(container):
    return 'docker rm -f {}'.format(container)

def docker_run(setting):
    command = 'docker run -d'
    if 'name' in setting:
        command += ' --name={}'.format(setting['name'])
    if 'port' in setting: 
        command += ' -p {}:{}'.format(setting['port']['host'], setting['port']['cont'])
    for key, value in setting.get('env', dict()).items():
        command += ' --env {}={}'.format(key, value)
    command += ' {}'.format(setting.get('docker', ''))
    return command

if args.action == 'start':
    containers = [execute(docker_run(container).split(' ')) for container in setting]
    list(map(print, containers))
    if all(container for container in containers):
        pickle.dump(containers, open('containers.p', 'wb'))
        print ('All container started!')
    else:
        print ('Error raised while starting')
elif args.action == 'stop':
    containers = pickle.load(open('containers.p', 'rb'))
    results = [execute(docker_stop(container).split(' ')) for container in containers]
    list(map(print, results))
    if all(result for result in results):
        print ('All container stopped!') 
    else:
        print ('Error raised while stoping')
