import shlex
import os
import logging

log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())

_proc_environ = os.environ.copy()

def shell_vars_str_to_dict(shell_vars_data):
    """
    Returns the given shell vars string as a dictionary
    """
    log.info("converting shell variable str to dict")
    shell_vars = dict(token.split('=',1) for token in shlex.split(shell_vars_data))
    return shell_vars

def sh_command_env(command_env):
    """
    Helper to prepare sh.Command _env dict.
    """
    cmd_env = command_env
    cmd_env.update(_proc_environ)
    return cmd_env

def get_files(paths, extension):
    found_files = []
    for path in paths:
        for root, dirs, files in os.walk(path):
            for f in files:
                if f.endswith(extension):
                    found_files.append(os.path.join(root, f))
    return found_files
