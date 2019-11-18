import subprocess


def run_playbook(playbook_filename, hosts, playbook_command='ansible-playbook', private_key=None, extra_options=None, extra_vars=None):

    command = construct_playbook_command(playbook_filename, hosts, playbook_command=playbook_command, private_key=private_key,extra_options=extra_options, extra_vars=extra_vars)

    process = subprocess.Popen(command, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    return (process.wait(), process.stdout.read(), process.stderr.read())


def get_hosts_str(hosts):
    if isinstance(hosts, list):
        hosts = ",".join(hosts) + ","

    if not isinstance(hosts, str):
        raise TypeError('hosts must be a str or list object')

    return hosts


def construct_playbook_command(playbook_filename, hosts, playbook_command='ansible-playbook', private_key=None, extra_options=None, extra_vars=None):

    hosts = get_hosts_str(hosts)

    command = [
        playbook_command,
        playbook_filename,
        '-i',
        hosts,
    ]

    if private_key:
        command.append('--private-key={}'.format(private_key))

    if extra_vars:
        vars = ' '.join("{}={}".format(key, value) for (key, value) in sorted(extra_vars.items()))
        command += ['--extra-vars', vars]

    if not extra_options:
        return command

    if isinstance(extra_options, str):
        command.append(extra_options)
    elif isinstance(extra_options, list):
        command += extra_options
    else:
        raise TypeError("extra_options must be str or list.")

    return command


def run_ping(host, ansible_command='ansible'):

    command = construct_ping_command(host, ansible_command=ansible_command)

    process = subprocess.Popen(command, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    return (process.wait(), process.stdout.read(), process.stderr.read())


def construct_ping_command(host, ansible_command='ansible'):

    host = get_hosts_str(host)

    command = [
        ansible_command,
        'all',
        '-i',
        host,
        '-m',
        'ping'
    ]

    return command
