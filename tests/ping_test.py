import unittest
from ansible_subprocess.main import construct_ping_command, run_ping


class PingCommandTest(unittest.TestCase):

    def test_construct_ping_command(self):
        command = construct_ping_command('127.0.0.1')
        self.assertEqual(
            command,
            [
                'ansible',
                '127.0.0.1',
                '-m',
                'ping'
                ]
        )

    def test_construct_ping_command_with_specific_ansible_command(self):
        command = construct_ping_command('127.0.0.1', ansible_command='/bin/ansible')
        self.assertEqual(
            command,
            [
                '/bin/ansible',
                '127.0.0.1',
                '-m',
                'ping'
                ]
        )


class PingTest(unittest.TestCase):

    def test_ping_to_localhost(self):
        status, stdout, stderr = run_ping('localhost')
        self.assertEqual(status, 0)
        self.assertTrue('pong' in stdout)
        self.assertEqual(stderr, '')
