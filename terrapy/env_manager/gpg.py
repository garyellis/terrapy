from terrapy.env_manager import utils
import gnupg
import logging
import os


def gpg_decrypt(gpg_file):
    """
    Decrypts the given input gpg file as a string
    """
    gpg = gnupg.GPG()
    with open(gpg_file) as f_stream:
        log.info('decrypting {}'.format(gpg_file))
        decrypted_data = gpg.decrypt_file(f_stream)
        return str(decrypted_data)

def get_gpg_env(dest_dirs):
    """
    """
    gpg_env = {}
    gpg_files = utils.get_files(dest_dirs, '.gpg')
    for f in gpg_files:
        gpg_env_str = gpg_decrypt(f)
        gpg_env.update(utils.shell_vars_str_to_dict(gpg_env_str))
    return utils.sh_command_env(gpg_env)
