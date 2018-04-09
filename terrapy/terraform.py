import sh
from sh import ErrorReturnCode
from sh import terraform, Command
go_getter = Command("go-getter")
import logging
import os
import re

log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())

TF_OUTPUT_OFFSET = 16
TF_DEFAULT_ARGS = {
    'v0.11.3': {
        'plan': [],
        'validate': ['-check-variables=false'],
        'apply': []
    },
    'v0.11.6': {
        'plan': ['-no-color'],
        'validate': ['-check-variables=false'],
        'apply': ['-force']
    },
    'unsupported_version': {
        'plan': [],
        'validate': [],
        'apply': []
    }
}

class Terraform(object):
    def __init__(self, environment, tf_module_path, tf_args, overwrite_default_args=False, dry_run=False):
        self.tf_module_path = tf_module_path
        self.version = get_tf_version(tf_module_path)
        self.environment = environment
        self.tf_args = tf_args
        self.overwrite_default_args = overwrite_default_args
        self.dry_run = dry_run

    def run(self, command):
        self.command = command
        tf_args = self.tf_args[:]
        with sh.pushd(self.tf_module_path):
            try:
                if not self.overwrite_default_args:
                    log.info('Merging {} default and user provided args'.format(command))
                    tf_args = TF_DEFAULT_ARGS[self.version].get(command, []) + tf_args

                tf_args.insert(0, command)
                if self.dry_run:
                    log.info('Dry run enabled.')
                    log.info('Would run: terraform {}'.format(" ".join(tf_args)))
                else:
                    terraform(tf_args)
            except ErrorReturnCode as err:
                log.error(err.stderr)

def get_tf_version(tf_module_path):
    """
    """
    tf_version = ""
    tf_version_re='^Terraform\s.*?(?=\w+)(v.*[0-9.]+)'
    with sh.pushd(tf_module_path):
        m = re.findall(
            tf_version_re,
            str(terraform.version())
        )

        if m:
            tf_version = m[0]
            log.info('detected terraform {}'.format(tf_version))
            return tf_version

def format_tf_output(output):
    return re.sub(r'(?m)^', ' ' * TF_OUTPUT_OFFSET, str(output))
