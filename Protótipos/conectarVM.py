from fabric import Connection
with Connection('192.168.100.12', port=22, user='mininet', connect_kwargs={'password': 'mininet'}) as c:
    c.run('sudo mn --topo minimal', pty=True)
