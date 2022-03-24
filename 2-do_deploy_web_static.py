#!/usr/bin/python3
"""distributes an archive to your web servers, using the function do_deploy"""

from fabric.api import put, run, env
from os.path import exists


env.hosts = ['44.200.42.30', '18.210.27.59']


def do_deploy(archive_path):
    '''distributes an archive to my web servers'''
    if not exists(archive_path):
        return False
    try:
        file_name = archive_path.split("/")[-1].split(".")[0]
        put(archive_path, "/tmp/")

        run("mkdir -p /data/web_static/releases/{}".format(file_name))

        run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/"
            .format(file_name, file_name))

        run('rm -rf /tmp/{}.tgz'.format(file_name))

        run(('mv /data/web_static/releases/{}/web_static/* ' +
             '/data/web_static/releases/{}/')
            .format(file_name, file_name))

        run('rm -rf /data/web_static/releases/{}/web_static'
            .format(file_name))

        run('rm -rf /data/web_static/current')

        run(('ln -s /data/web_static/releases/{}/' +
             ' /data/web_static/current')
            .format(file_name))
        return True
    except Exception:
        return False
