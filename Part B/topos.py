"""

Mininet Topologies with 10 nodes 
Author : Shreshth Tuli

Usage:

1. Linear Topology
    - sudo mn --custom topos.py --topo linear
2. Ring Topology
    - sudo mn --custom topos.py --topo ring --controller=remote,ip=127.0.0.1
3. Mesh Topology
    - sudo mn --custom topos.py --topo mesh --controller=remote,ip=127.0.0.1
4. Star Topology
    - sudo mn --custom topos.py --topo star

To specify parameters use: --link tc,bw=10,delay=3,loss=2,max_queue_size=3

Example : for ring topology with bandwidth limited to 2:
	- sudo mn --custom topos.py --topo linear --controller=remote,ip=127.0.0.1 --link tc,bw=10

"""

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

class LinearTopo( Topo ):
    "Linear Topology Mininet"

    def __init__( self ):

        # Initialize topology
        Topo.__init__( self )

        hosts = []
        switches = []

        for x in range(0, 10):

            # Add hosts and switches
            hosts.append(self.addHost( 'h%s' % (x+1) ))
            switches.append(self.addSwitch( 's%s' % (x+1) ))

            # Add links in linear topology

            # Connecting hosts to switches
            self.addLink(hosts[x], switches[x])
            # Connecting switches in linear order
            if(x > 0):
                self.addLink(switches[x-1], switches[x])


class RingTopo( Topo ):
    "Ring Topology Mininet"

    def __init__( self ):

        # Initialize topology
        Topo.__init__( self )

        hosts = []
        switches = []

        for x in range(0, 10):

            # Add hosts and switches
            hosts.append(self.addHost( 'h%s' % (x+1) ))
            switches.append(self.addSwitch( 's%s' % (x+1) ))

            # Add links in linear topology

            # Connecting hosts to switches
            self.addLink(hosts[x], switches[x])
            # Connecting switches in ring order
            if(x > 0):
                self.addLink(switches[x-1], switches[x])

        self.addLink(switches[0], switches[9])


class MeshTopo( Topo ):
    "Mesh Topology Mininet"

    def __init__( self ):

        # Initialize topology
        Topo.__init__( self )

        hosts = []
        switches = []

        for x in range(0, 10):

            # Add hosts and switches
            hosts.append(self.addHost( 'h%s' % (x+1) ))
            switches.append(self.addSwitch( 's%s' % (x+1) ))

            # Add links in mesh topology

            # Connecting hosts to switches
            self.addLink(hosts[x], switches[x])
            # Connecting switches in mesh order

        for x in range(0, 10):
            # Connecting switches in mesh order
            for y in range(x+1, 10):
                self.addLink(switches[x], switches[y])


class StarTopo( Topo ):
    "Star Topology Mininet"

    def __init__( self ):

        # Initialize topology
        Topo.__init__( self )

        hosts = []
        # Add common switch
        switch = self.addSwitch( 's1' )

        for x in range(0, 10):
            # Add hosts
            hosts.append(self.addHost( 'h%s' % (x+1) ))
            # Connect host and switch
            self.addLink(hosts[x], switch)
   

topos = { 
 'linear': ( lambda: LinearTopo() ),
 'ring': ( lambda: RingTopo() ) ,
 'mesh': ( lambda: MeshTopo() ) ,
 'star': ( lambda: StarTopo()) 
  }