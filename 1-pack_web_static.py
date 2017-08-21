#!/usr/bin/python3
""" 
Compress file
"""
import time
from fabric.api import local, run, hosts, env

def do_pack():
    """
    do_pack - method that compresses the files
    """
    deploy_time = time.strftime("%Y%m%d%H%M%S")
    new_tar_file = "web_static_" + deploy_time + ".tgz" 
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/{} web_static".format(new_tar_file))
        return ("versions/{}".format(new_tar_file))
    except:
        return None
