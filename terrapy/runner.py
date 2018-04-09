import terrapy.config
import terrapy.env_manager
import terrapy.terraform

log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())

class Terraformer(object):
    def __init__(self, command, command_args=[], tf_module_path=None, tf_module_config=None):
        self.command = command
        self.command_args = command_args
        self.tf_module_path = tf_module_path
        self.config = terrapy.config.get_module_config(tf_module_config)
        self.terraform = terrapy.terraform.Terraform(tf_module_path)
        self.env_sources_list = []
        self.environ = {}

    def get_config(self, tf_module_config):
        """
        """
        return terrapy.config.get_module_config(tf_module_path)

    def get_env_sources(self):
        """
        """
        self.env_sources_list = self.config['env']['sources']
        return terrapy.getter.py_get_items(self.env_sources_list)

    def setup_environment(self):
        """
        """
        self.env_sources = self.get_env_sources()
        self.environ.update(
            terrapy.env_manager(self.env_sources)
        )
        

    def execute(self, action):
        """
        """
        if self.config['enabled']:
            log.info("preparing environment for {} on {}.".format(self.command, self.tf_module_path))
            self.setup_environment()

            log.info("running {} on {}".format(self.command, self.tf_module_path))
            getattr(self.terraform, command)(*args, **kwargs)

        else:
            log.info('Skipping {} on {}. Config enabled is false.'.format(self.command, self.tf_module_path))
