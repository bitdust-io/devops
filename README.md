# BitDust DevOps

Collection of tools, scripts and helpers for maintaining BitDust infrastracture


Usage
=====

Prepare environment
-------------------

```shell
    $ make venv
```


Install/update telegraf configuration
-------------------------------------

1. Monitoring machine has different telegraf location (localhost one)

```shell
    $ ansible-playbook ansible/telegraf.yml -i ansible/inventory/test -K --limit monitoring -e "application_name=monitoring"
```

2. Machine with broken apt dependencies

```shell
    $ ansible-playbook ansible/telegraf.yml -i ansible/inventory/test -K --limit nodes_broken_apt -e "application_name=broken_apt"
```

3. Fully functional machines

```shell
    $ ansible-playbook ansible/telegraf.yml -i ansible/inventory/test --limit nodes -e "application_name=main"
```

Playground
==========

Run
---

```shell
    $ cd playground
    $ docker-compose up
    ...
    $ docker-compose down -v
    
```

Create testing network
----------------------

```shell
    $ ansible-playbook ansible/bitdust.yml -i ansible/inventory/docker --limit nodes
```


Install telegraf
----------------

```shell
    $ ansible-playbook ansible/telegraf.yml -i ansible/inventory/docker --limit nodes -e "application_name=main"
```
