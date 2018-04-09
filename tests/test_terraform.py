import re
import pytest
import terrapy.terraform


class TestTerraform(object):
    
    def test_get_tf_version(self):
        tf_version_0_11_3 = 'v0.11.3'
        assert tf_version_0_11_3 == terrapy.terraform.get_tf_version('./tests/fixtures/tf_0.11.3/')
        tf_version_0_11_6 = 'v0.11.6'
        assert tf_version_0_11_6 == terrapy.terraform.get_tf_version('./tests/fixtures/tf_0.11.6/')

    def test_format_tf_output(self):
        tf_output = """

Apply complete! Resources: 0 added, 0 changed, 0 destroyed.

Outputs:

foo = bar
"""
        m = re.findall(
            r'^(\s{16})',
            terrapy.terraform.format_tf_output(tf_output),
            re.MULTILINE
        )
        print tf_output
        assert len(m) == 8

    def test_terraform(self):
        terraform = terrapy.terraform.Terraform(
            environment={},
            tf_module_path='./tests/fixtures/tf',
            tf_args=[],
            overwrite_default_args=False,
            dry_run=False
        )
        terraform.dry_run = True
        terraform.run(command='plan')

        terraform.dry_run = False
        terraform.run(command='plan')
        terraform.tf_args = ['-var', 'foo=bar']
        terraform.run(command='plan')
