# BitDust DevOps

Collection of tools, scripts and helpers for maintaining BitDust infrastracture


Usage
=====

```shell
    $ make venv
    $ cd ansible
```


Install/update telegraf configuration on monitoring machine
-----------------------------------------------------------
```shell
ansible-playbook telegraf.yml -i inventory/test -K --limit monitoring -e "application_name=monitoring"
```


Install/update telegraf configuration on nodes with broken dependencies
-----------------------------------------------------------------------

```shell
ansible-playbook telegraf.yml -i inventory/test -K --limit nodes_broken_apt -e "application_name=broken_apt"
```


Playground
----------

```shell
ansible-playbook ansible/telegraf.yml -i ansible/inventory/docker --limit nodes -e "application_name=main"
```
