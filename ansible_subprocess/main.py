import subprocess


def run_playbook(playbook_filename, hosts, playbook_cmd='ansible-playbook', private_key=None, **extra_vars):

    command = construct_playbook_command(playbook_filename, hosts, playbook_cmd, private_key, extra_vars)

    process = subprocess.Popen(command, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    return (process.wait(), process.stdout.read(), process.stderr.read())


def construct_playbook_command(playbook_filename, hosts, playbook_command='ansible-playbook', private_key=None, extra_vars=None):
    hosts = ",".join(hosts) + ","

    command = [
        playbook_command,
        playbook_filename,
        '-i',
        hosts,
    ]

    if extra_vars:
        vars = ' '.join("{}={}".format(key, value) for (key, value) in extra_vars.keys())
        command.extend(['--extra-vars', vars])

    return command


def run_ping(host):

    command = [
        'ansible',
        host,
        '-m',
        'ping'
    ]

    process = subprocess.Popen(command, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    return (process.wait(), process.stdout.read(), process.stderr.read())


def construct_ping_command(host, ansible_command):

    command = [
        ansible_command,
        host,
        '-m',
        'ping'
    ]

    return command
