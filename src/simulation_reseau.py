from mininet.net import Mininet
from mininet.node import OVSSwitch
from mininet.link import TCLink
from mininet.topo import Topo


class ReseauTopo(Topo):

    def build(self):
        
        switch= self.addSwitch('sw1')

        h1= self.addHost('h1')
        h2= self.addHost('h2')
        h3= self.addHost('h3')

        self.addLink(h1, switch, cls= TCLink)
        self.addLink(h2, switch, cls=TCLink)
        self.addLink(h3, switch, cls= TCLink)

def simulation_reseau():
    topo= ReseauTopo()
    net=Mininet(topo=topo, switch= OVSSwitch, link= TCLink)
    net.start()

    h1=net.get('h1')
    h2=net.get('h2')
    h3=net.get('h3')


    h1.cmd('mkdir -p /tmp/logs_systeme && python3 /home/mg89dva01/Documents/Systeme-Distribue/src/http_server.py > /tmp/logs_systeme/h1.log 2>&1 &')
    h2.cmd('mkdir -p /tmp/logs_systeme && python3 /home/mg89dva01/Documents/Systeme-Distribue/src/worker.py > /tmp/logs_systeme/h2.log 2>&1 &')
    h3.cmd('mkdir -p /tmp/logs_systeme && python3 /home/mg89dva01/Documents/Systeme-Distribue/src/worker.py > /tmp/logs_systeme/h3.log 2>&1 &')   

    # Dans le script, après net.start() et avant net.stop() :
    print(h1.cmd('ping -c 3 10.0.0.2'))  # ping h2
    print(h1.cmd('ping -c 3 10.0.0.3'))  # ping h3   


if __name__== '__main__':
    simulation_reseau()



