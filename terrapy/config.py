import yaml
import logging

log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())

def validate_module_config(f):
    """
    """
    pass

def get_module_config(f):
    """
    """
    with open(f, 'r') as s:
        log.info('opening config {}'.format(f))
        try:
            config = yaml.load(s)
            return config
        except:
            raise Exception("bad config")
            

def load_module_configs(config_files):
    """
    """
    config = []
    for c in config_files:
        config.append({'name': c, 'properties': get_module_config(c)})
    return config
