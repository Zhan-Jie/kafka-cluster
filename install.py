import json
import os
import subprocess

# base directory of current script
basedir = os.path.split(os.path.realpath(__file__))[0]

def call(cmd = ""):
    shell = subprocess.Popen(cmd, shell=True)
    shell.wait()
    return shell.returncode

def read_config():
    config = {}
    with open(basedir + '/config.json', 'r') as f :
        config = json.load(f)
    return config

def gen_hosts(config = {}):
    hosts_str = '[zookeeper]\n'
    zk_hosts = config['zookeeper_hosts']
    for i in range(len(zk_hosts)):
        hosts_str += '{} my_id="{}"\n'.format(zk_hosts[i], i+1)
    
    hosts_str += '\n[kafka]\n'
    kafka_hosts = config['kafka_hosts']
    for i in range(len(kafka_hosts)):
        hosts_str += '{} broker_id="{}"\n'.format(kafka_hosts[i], i+1)
    
    hosts_str += '\n[all:children]\n'
    hosts_str += 'kafka\nzookeeper\n\n'

    hosts_str += '[all:vars]\n'
    hosts_str += 'java_home="{}"\n'.format(config['java_home'])
    hosts_str += 'temp_dir="/tmp"\n'
    hosts_str += 'zk_home="{}"\n'.format(config['zookeeper_home'])
    hosts_str += 'zk_data_dir="{}"\n'.format(config['zookeeper_data_dir'])
    hosts_str += 'kafka_home="{}"\n'.format(config['kafka_home'])
    hosts_str += 'kafka_log_dir="{}"\n'.format(config['kafka_log_dir'])

    with open(basedir + '/hosts', 'w') as f :
        f.write(hosts_str)

if __name__ == '__main__' :
    gen_hosts(read_config())
    code = call('ansible-playbook -i {}/hosts {}/install.yml'.format(basedir, basedir))
    if code == 0 :
        print('======= INSTALLATION FINISHED =======')
    else :
        print('======= INSTALLATION FAILED =======')

    print('HINT: uninstall with following command')
    print('ansible-playbook -i {}/hosts {}/clean.yml'.format(basedir, basedir))
    
