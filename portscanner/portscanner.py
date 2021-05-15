import socket
from IPy import IP  # https://github.com/autocracy/python-ipy/

def scan(target):
    converted_ip = check_ip(target)
    print('\n' + f'[-_0 Scanning Target] {target}')
    for port in range(1,500):
        scan_port(converted_ip, port)

def check_ip(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)

def get_banner(s):
    return s.recv(1024)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            print(f'[+] Open Port {port} : ' + str(banner.decode().strip('\n')))
        except:
            print(f'[+] Open Port {port}')
    except:
        pass

# GET IP
# $ nslookup www.arh.bg.ac.rs
# 147.91.19.26
# testphp.vulnweb.com 18.192.172.30

if __name__ == "__main__":
    targets = input('[+] Enter Target/s To Scen(split multiple targets with ,): ')
    if ',' in targets:
        for ip_add in targets.split(','):
            scan(ip_add.strip(' '))
    else:
        scan(targets)
