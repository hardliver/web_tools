import portscanner

targets_ip = input('[+] * Enter Target To Scan For Vulnerable Open Ports: ')
port_number = int(input('[+] * Enter Amount Of Ports You Want To Scan(500 - first 500 ports): '))
vul_file = input('[+] * Enter Path To The File With Vulnerable Softwares: ')
print('\n')

target = portscanner.PortScan(targets_ip, port_number)
target.scan()

print('banners', target.banners)
print('open_ports', target.open_ports)

with open(vul_file, 'r') as file:
    for count, banner in enumerate(target.banners):
        file.seek(0)
        for line in file.readlines():
            if line.strip() in banner:
                print(f'[!!] VULNERABLE BANNER: "{banner}" ON PORT: {str(target.open_ports[count])}')

# testphp.vulnweb.com
# vulbanners.txt
