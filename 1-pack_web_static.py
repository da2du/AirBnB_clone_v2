#!/usr/bin/python3
"""a Fabric script that generates a .tgz archive"""
from datetime import datetime
from fabric.operations import local


def do_pack():
    """A method"""
    local("mkdir -p versions")
    Arc = "versions/web_static_{}.tgz".format(datetime.now()
                                               .strftime("%Y%m%d%H%M%S"))
    name = local("tar -cvzf {} web_static".format(Arc))
    if name.failed:
        return None
    return name
