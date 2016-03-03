 # -*- coding: utf-8 -*-
from fabric.api import *
import fabric.contrib.project as project
import os
import shutil
import sys
import SocketServer
import paramiko

from pelican.server import ComplexHTTPRequestHandler

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'output'
DEPLOY_PATH = env.deploy_path

# Remote path configuration
env.dest_path = 'web'
DEST_PATH = env.dest_path

# Remote server configuration
production = '88.174.237.132'

# Git configuration
env.github_name = "origin"
env.local_branch = "master"

# Port for `serve`
PORT = 8000
# Port for `publish`
PORTR = 6003

def clean():
    """Remove generated files"""
    if os.path.isdir(DEPLOY_PATH):
        shutil.rmtree(DEPLOY_PATH)

def build():
    """Build local version of site"""
    local('pelican -s pelicanconf.py')

def rebuild():
    """`clean` then `build`"""
    clean()
    build()

def regenerate():
    """Automatically regenerate site upon file modification"""
    local('pelican -r -s pelicanconf.py')

def serve():
    """Serve site at http://localhost:8000/"""
    os.chdir(env.deploy_path)

    class AddressReuseTCPServer(SocketServer.TCPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(('', PORT), ComplexHTTPRequestHandler)

    sys.stderr.write('Serving on port {0} ...\n'.format(PORT))
    server.serve_forever()

def reserve():
    """`build`, then `serve`"""
    build()
    serve()

def preview():
    """Build production version of site"""
    local('pelican -s publishconf.py')

@hosts(production)
def publish():
    """Publishing on GitHub and synology server"""
    rebuild()
    local("git checkout -q master")
    local("git fetch {github_name}".format(**env))
    local("git push {github_name} {local_branch} ".format(**env))
    # print 'connection à Synology : déploiement avec put après connection'
    local('sftp -P '+PORTR+' {production}:{dest_path}'.format(**env))
#   project.rsync_project(
        # remote_dir=dest_path,
        # exclude=[".*"],
        # local_dir=DEPLOY_PATH.rstrip('/') + '/',
        # delete=True,
        # extra_opts='-c',
    # )
