import yaml
import pytest
import mock
from mock import mock_open

import terrapy.config

config = """
---
enabled: true
apply_group: 1-10
depends_on: []
secrets:
- 'git@github.com:garyellis/gpg_secrets.git?ref=masterFFFF//gpg_secrets'
- 'git@github.com:garyellis/gpg_secrets.git?ref=master//gpg_secrets'
terraform_version: v0.11.3
terraform_binary:
terraform_docker_image: terraform:/v0.11.3
terraform_args: []
pre_scripts:
post_scripts:
"""

bad_config = """
{
  enabled true
}
"""

class TestConfig(object):

    @mock.patch("__builtin__.open", mock_open(read_data=config))
    def test_get_module_config(self):
        f = terrapy.config.get_module_config("file.yml")
        print f['enabled']

    @mock.patch("__builtin__.open", mock_open(read_data=bad_config))
    def test_get_module_config_bad(self):
        with pytest.raises(KeyError, ):
            f = terrapy.config.get_module_config("file.yml")
            print f['enabled']
