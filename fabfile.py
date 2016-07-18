from fabric.api import *
from pytz import timezone
from fabric.contrib.files import exists
from fabric.contrib.project import rsync_project
from datetime import datetime
from os import path
import config.env


def backup(dbname=None, dbuser=None, dbpass=None, remote_backup_path=None, local_backup_path=None):
    validate_args([dbname, dbuser, dbpass])

    def_back_path = '/tmp/bak/' + dbname + '/'
    remote_backup_path = remote_backup_path or def_back_path
    local_backup_path = local_backup_path or def_back_path

    if not exists(remote_backup_path):
        run('mkdir -p ' + remote_backup_path)

    if not path.exists(local_backup_path):
        local('mkdir -p ' + local_backup_path)

    bak_filename = get_bak_filename()
    full_back_path = remote_backup_path + bak_filename

    run('mysqldump -u ' + dbuser + ' --password=' + dbpass + ' ' + dbname + ' > ' + full_back_path)

    files = run('ls ' + remote_backup_path + ' | sort', quiet=True).split()

    if len(files) > env.max_backups:
        run('rm -f ' + "{}/{}".format(remote_backup_path, files[0]))

    rsync_project(remote_backup_path, local_dir=local_backup_path, upload=False, delete=True, default_opts='-pthrz')


def validate_args(args=None):
    if args is not None:
        for arg in args:
            if arg is None:
                abort('Required parameters: dbname, dbuser, dbpass')


def get_bak_filename():
    timestamp = datetime.now(tz=timezone('Japan')).replace(microsecond=0, tzinfo=None).isoformat().replace(':', '')
    return timestamp + '.sql'
