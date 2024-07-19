i#!/usr/bin/python3

from fabric.api import *
from fabric.state import commands, connections
import os


env.user = 'ubunut'
env.hosts = [""]

def do_clean(number=0):
    local('ls -t ~/AirBnB_clone_v2/versions/').split()
    with cd("/data/web_static/releases"):
        target_n = sudo("ls -t .").split()

    paths = "/data/web_static/releases"
    number = int(number)

    if number == 0 :
        num = 1
    else:
        num = number

    if len(target_R) > 0:
        if len(target) == number or len(target) == 0:
            pass
        else:
            cl = target[num:]
            for i in range(len(cl)):
                local('rm -f ~/AirBnB_Clone_V2/versions/{}'.format(target[-1]))
        rem = target_R[num:]
        for j in range(len(rem)):
            sudo('rm -rf {}/{}'.format(paths, rem[-1].strip(".tgz")))
    else:
        pass
