Role Name
=========

This role deploys zookeeper and kafka containers as standalone or HA.

Requirements
------------

- Docker daemon must be installed and running in the host
- Vagrant required in the execution PC
- Python required in the execution PC



### Setup

```
virtualenv -p $(which python) .venv
. .venv/bin/activate
```

### Tests execution

```
molecule create
molecule converge
molecule idempotence
molecule verify
```

### Environment destroy

```
molecule destroy
```
