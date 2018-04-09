from sh import Command
go_getter = Command("go-getter")
from sh import ErrorReturnCode
import logging
import os

log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())


def _go_get(src, dest):
    """
    Wraps hashicorp go-getter cli https://github.com/hashicorp/go-getter
    """
    try:
        go_getter(src, dest)
    except ErrorReturnCode as err:
        log.error(err.stderr)

def py_get(src, dest):
    """
    Tiny py_get interface
    """
    try:
        log.info('get {}'.format(src))
        _go_get(src, dest)
    except Exception:
        log.error('failed')

def py_get_items(sources, dest):
    """
    """
    local_dest_work_dir = '{}/.sources'.format(dest)
    local_dest_dirs = []
    for i, src in enumerate(sources):
        local_dest_dir = '{}/{}'.format(local_dest_work_dir,i)
        try:
            log.info('fetching {}'.format(src))
            py_get(i, local_dest_dir)
            local_dest_dirs.append(local_dest_dir)
        except ErrorReturnCode as err:
            log.error(err.stderr)
    return local_dest_dirs
