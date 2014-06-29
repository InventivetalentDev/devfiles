from fabric.api import *
from fabric.contrib import *
from fabfile.common import *
from fabfile import apps

@task
def install():
    '''
    Node.js BukGet API Implimentation installer
    '''
    dl_template('upstart_nodeapi.conf', '/etc/init/nodeapi.conf')
    with cd('/opt'):
        run('git clone git://github.com/BukGet/api.git nodeapi')
    with cd('/opt/nodeapi'):
        run('npm install')


@task
def upgrade():
    with cd('/opt/nodeapi'):
        run('git pull')
    restart()


@task
def start():
    run('initctl start nodeapi')


@task
def stop():
    run('initctl stop nodeapi')


@task
def restart():
    stop()
    start()