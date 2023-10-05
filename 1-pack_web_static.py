#!/usr/bin/python3
# Fabric script that generates a .tgz archive from the contents of web_static

from fabric import task
from datetime import datetime
import os


@task
def do_pack():
    """Generate a .tgz archive from the contents of web_static folder."""
    timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    archive_name = f"web_static_{timestamp}.tgz"
    local_folder = "web_static"
    archive_folder = "versions"

    # Create the versions folder if it doesn't exist
    if not os.path.exists(archive_folder):
        os.makedirs(archive_folder)

    # Create the archive using tar command
    tar_command = f"tar -czvf {archive_folder}/{archive_name} {local_folder}"

    result = local(tar_command)

    if result.failed:
        return None
    return f"{archive_folder}/{archive_name}"
