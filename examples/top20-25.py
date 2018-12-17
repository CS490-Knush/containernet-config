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
c1 = net.addDocker('c1', ip='10.0.0.251', dimage="knush/finished-server:latest")
c2 = net.addDocker('c2', ip='10.0.0.252', dimage="knush/finished-server:latest")

st3 = net.addDocker('st3', ip='10.0.0.253', dimage="knush/finished-server:latest")
st4 = net.addDocker('st4', ip='10.0.0.254', dimage="knush/finished-server:latest")

info('*** Adding switches\n')
s1 = net.addSwitch('s1')
s2 = net.addSwitch('s2')
s3 = net.addSwitch('s3')
s4 = net.addSwitch('s4')
s5 = net.addSwitch('s5')
s6 = net.addSwitch('s6')
s7 = net.addSwitch('s7')
s8 = net.addSwitch('s8')

info('*** Creating links\n')
# hosts
net.addLink(c1, s1, cls=TCLink, bw = 25, use_tbf = True)
net.addLink(c2, s6, cls=TCLink, bw = 25, use_tbf = True)
net.addLink(st3, s3, cls=TCLink, bw = 25, use_tbf = True)
net.addLink(st4, s8, cls=TCLink, bw = 25, use_tbf = True)

# top
net.addLink(s1, s2, cls=TCLink, bw = 20, use_tbf = True)
net.addLink(s2, s3, cls=TCLink, bw = 20, use_tbf = True)

# bottom
net.addLink(s6, s7, cls=TCLink, bw = 20, use_tbf = True)
net.addLink(s7, s8, cls=TCLink, bw = 20, use_tbf = True)

# X
net.addLink(s1, s4, cls=TCLink, bw = 25, use_tbf = True)
net.addLink(s3, s5, cls=TCLink, bw = 25, use_tbf = True)
net.addLink(s4, s6, cls=TCLink, bw = 25, use_tbf = True)
net.addLink(s5, s8, cls=TCLink, bw = 25, use_tbf = True)

# shared
net.addLink(s4, s5, cls=TCLink, bw = 25, use_tbf = True)

info('*** Starting network\n')
net.start()
info('*** Testing connectivity\n')
net.ping([c1, c2, st3, st4])
# info('*** Running CLI\n')
# CLI(net)
# info('*** Stopping network')
# net.stop()

