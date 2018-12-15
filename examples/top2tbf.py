#!/usr/bin/python
"""
This is the most simple example to showcase Containernet.
"""
from mininet.net import Containernet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import info, setLogLevel
setLogLevel('info')

net = Containernet(controller=RemoteController)
info('*** Adding controller\n')
net.addController('c0', ip='127.0.0.1')
info('*** Adding docker containers\n')
d1 = net.addDocker('d1', ip='10.0.0.251', dimage="knush/custom-spark-only:v1")
d2 = net.addDocker('d2', ip='10.0.0.252', dimage="knush/custom-spark-only:v1")
info('*** Adding switches\n')
s1 = net.addSwitch('s1')
info('*** Creating links\n')
net.addLink(d1, s1, cls=TCLink, bw = 50, use_tbf=True)
net.addLink(s1, d2, cls=TCLink, bw = 30, use_tbf=True)

info('*** Starting network\n')
net.start()
info('*** Testing connectivity\n')
net.ping([d1, d2])
info('*** Running CLI\n')
CLI(net)
info('*** Stopping network')
net.stop()

