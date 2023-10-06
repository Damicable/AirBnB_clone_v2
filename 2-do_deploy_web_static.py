#!/usr/bin/python3
"""
Fabric script That distribute an archive to web servers.
"""

from fabric import task
from datetime import datetime
import os

env.hosts = ['34.224.62.116', '35.174.204.80']
env.user = 'ubuntu'


@task
def do_deploy(archive_path):
    """
    Distribute and deploy an archive to web servers.

    Args:
        archive_path (str): The path to the archive to be deployed.

    Returns:
        bool: True if all operations have been done correctly, False otherwise.
    """
    if not os.path.exists(archive_path):
        return False

    try:
        """ Upload the archive to /tmp/ on the web server"""
        archive_filename = os.path.basename(archive_path)
        tmp_archive_path = "/tmp/" + archive_filename
        put(archive_path, tmp_archive_path)

        """ Create a directory for the new release"""
        release_folder = "/data/web_static/releases/" + \
            archive_filename.split('.')[0]
        run("mkdir -p {}".format(release_folder))

        """ Uncompress the archive to the release folder"""
        run("tar -xzf {} -C {}".format(tmp_archive_path, release_folder))

        """ Delete the archive from /tmp/"""
        run("rm -f {}".format(tmp_archive_path))

        """ Move the contents to the current symbolic link"""
        run("mv {}/web_static/* {}".format(release_folder, release_folder))

        """ Remove the empty web_static directory"""
        run("rm -rf {}/web_static".format(release_folder))

        """ Update the symbolic link"""
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(release_folder))

        return True
    except Exception as e:
