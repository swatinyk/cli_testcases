from datetime import datetime
import paramiko
import pytest
import logging

from paramiko.ssh_exception import NoValidConnectionsError
logging.basicConfig(level=logging.INFO)

@pytest.fixture
def setup():
    global client
    try:
        client=paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        key_file = paramiko.RSAKey.from_private_key_file('/home/gslab/.ssh/id_rsa')
        client.connect(hostname='127.0.0.1',port=2222,username='swati',pkey=key_file)
        yield client
    except NoValidConnectionsError as msg:
        logging.exception('connection to remote host failed',msg)
    finally:
        client.close()

@pytest.fixture
def get_filename(request):
    current_datetime = datetime.now()
    str_current_datetime = str(current_datetime)
    file_name= request.node.name+ str_current_datetime + ".log"
    yield  file_name

@pytest.mark.cli
def test_01_cpu(setup,get_filename):
    _, stdout, _ = setup.exec_command('iostat -c')
    res = stdout.read()
    logging.info('OUTPUT OF: iostat -c is {}'.format(res))
    s = res.split()
    cpu_utilization=s[-1].decode('utf-8')
    with open(get_filename, 'w') as f:
        f.write(str(res))

    assert 100-int(float(cpu_utilization)) < 90

@pytest.mark.cli
def test_02_memory(setup,get_filename):
    _, stdout, _ = setup.exec_command('cat /proc/meminfo')
    cmd_out=stdout.read()
    logging.info('OUTPUT OF :cat /proc/meminfo is {}'.format(cmd_out))
    s = cmd_out.split()
    total_memory=s[1].decode('utf-8')
    free_memory=s[4].decode('utf-8')
    memory_utilization=( (int(total_memory) - int(free_memory)) / int(total_memory) * 100 )
    with open(get_filename, 'w') as f:
        f.write(str(cmd_out))
    assert memory_utilization<90

@pytest.mark.cli
def test_03_disk(setup,get_filename):
    _, stdout, _ = setup.exec_command(' df -l --total')
    cmd_out=stdout.read()
    logging.info('OUTPUT OF :df -l --total is {}'.format(cmd_out))
    s = cmd_out.split()
    used_disk = s[-4].decode('utf-8')
    available_disk=s[-3].decode('utf-8')
    total_disk=used_disk+available_disk
    disk_used_percent = (int(used_disk) / int(total_disk)) * 100
    with open(get_filename, 'w') as f:
        f.write(str(cmd_out))
    assert disk_used_percent < 90.0

