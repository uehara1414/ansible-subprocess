import unittest
from ansible_subprocess.main import construct_playbook_command


class CommandTest(unittest.TestCase):

    def test_construct_playbook_command(self):
        command = construct_playbook_command('tests/playbooks/simple-playbook.yml', ['127.0.0.1'])
        self.assertEqual(
            command,
            [
                'ansible-playbook',
                'tests/playbooks/simple-playbook.yml',
                '-i',
                '127.0.0.1,'
                ]
        )

    def test_construct_playbook_command_with_host_name(self):
        command = construct_playbook_command('tests/playbooks/simple-playbook.yml', 'hosts')
        self.assertEqual(
            command,
            [
                'ansible-playbook',
                'tests/playbooks/simple-playbook.yml',
                '-i',
                'hosts'
            ]
        )

    def test_construct_playbook_command_with_specific_ansible_command(self):
        command = construct_playbook_command('tests/playbooks/simple-playbook.yml', ['127.0.0.1'], playbook_command='/bin/ansible-playbook')
        self.assertEqual(
            command,
            [
                '/bin/ansible-playbook',
                'tests/playbooks/simple-playbook.yml',
                '-i',
                '127.0.0.1,'
                ]
        )

    def test_construct_playbook_command_with_two_hosts(self):
        command = construct_playbook_command('tests/playbooks/simple-playbook.yml', ['127.0.0.1', '127.0.0.2'])
        self.assertEqual(
            command,
            [
                'ansible-playbook',
                'tests/playbooks/simple-playbook.yml',
                '-i',
                '127.0.0.1,127.0.0.2,'
                ]
        )

    def test_construct_playbook_command_with_extra_vars(self):
        command = construct_playbook_command('tests/playbooks/simple-playbook.yml', ['127.0.0.1', '127.0.0.2'], {"extra1": "var1", "extra2": "var2"})
        self.assertEqual(
            command,
            [
                'ansible-playbook',
                'tests/playbooks/simple-playbook.yml',
                '-i',
                '127.0.0.1,127.0.0.2,',
                '--extra-vars',
                '"extra1=var1 extra2=var2"'
                ]
        )

    def test_construct_playbook_command_with_private_key(self):
        command = construct_playbook_command('tests/playbooks/simple-playbook.yml', ['127.0.0.1'], private_key='/home/foo/id_rsa')
        self.assertEqual(
            command,
            [
                'ansible-playbook',
                'tests/playbooks/simple-playbook.yml',
                '-i',
                '127.0.0.1,',
                '--private-key=/home/foo/id_rsa'
                ]
        )

    def test_construct_playbook_command_with_extra_options(self):
        command = construct_playbook_command('tests/playbooks/simple-playbook.yml', ['127.0.0.1'], private_key='/home/foo/id_rsa', extra_options='--syntax-check')
        self.assertEqual(
            command,
            [
                'ansible-playbook',
                'tests/playbooks/simple-playbook.yml',
                '-i',
                '127.0.0.1,'
                '--private-key=/home/foo/id_rsa',
                '--syntax-check'
                ]
        )
