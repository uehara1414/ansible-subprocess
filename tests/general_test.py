import unittest

class GenericTest(unittest.TestCase):

    def test_import(self):

        import ansible_subprocess

    def test_accessible(self):

        import ansible_subprocess
        ansible_subprocess.run_playbook
        ansible_subprocess.run_ping
