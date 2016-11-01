import subprocess

def run_playbook(playbook_filename, hosts, playbook_cmd='ansible', private_key=None, **vars):

    hosts = ",".join(hosts) + ","

    command = [
        playbook_cmd,
        playbook_filename,
        '-i',
        hosts,
    ]

    if vars:
        extra_vars = ' '.join("{}={}".format(key, value) for (key, value) in vars.keys())
        command += ['--extra-vars', extra_vars]

    process = subprocess.Popen(command, stderr=subprocess.PIPE)

    return (process.wait(), process.stderr.read())

