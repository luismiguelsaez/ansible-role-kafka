import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_docker_service(host):
    assert host.ansible("service", "name=docker state=started")["changed"] is False

def test_kafka_running(host):
    kafka = host.docker("kafka")
    assert kafka.is_running

def test_zookeeper_running(host):
    zookeeper = host.docker("zookeeper")
    assert zookeeper.is_running