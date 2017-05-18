# ansible-subprocess
[![Build Status](https://travis-ci.org/uehara1414/ansible-subprocess.svg?branch=master)](https://travis-ci.org/uehara1414/ansible-subprocess)


[Not maintained!]ansible-subprocess run Ansible dynamically via the subprocess module.

## Demo

```python
from ansible_subprocess import run_playbook, run_ping
status, stdout, stderr = run_playbook('playbooks/sample.yml', 'web')
status, stdout, stderr = run_playbook('playbooks/sample2.yml',
                                      ['127.0.0.1', '127.0.0.2'],
                                      extra_vars={'var1': 'hoge', 'var2': 'fuga'},
                                      extra_options=['--syntax-check'])
status, stdout, stderr = run_ping(['8.8.8.8'])
```

## Installation

```bash
pip install ansible-subprocess
```

## License
[MIT](https://github.com/uehara1414/ansible-subprocess/blob/master/LICENSE)
