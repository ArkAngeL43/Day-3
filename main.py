import os, sys, time, datetime, psutil
import platform
from datetime import datetime
import psutil
import time as t # somehow the datetime fucks it up ``
from datetime import datetime
from subprocess import call
from prettytable import PrettyTable
import fcntl
import socket
import struct
from getmac import get_mac_address
from color import color

BLK       = "\033[0;30m"
RED       = "\033[0;31m"
GRN       = "\033[0;32m"
YEL       = "\033[0;33m"
BLU       = "\033[0;34m"
MAG       = "\033[0;35m"
CYN       = "\033[0;36m"
WHT       = "\033[0;37m"
BBLK      = "\033[1;30m"
BRED      = "\033[1;31m"
BGRN      = "\033[1;32m"
BYEL      = "\033[1;33m"
BBLU      = "\033[1;34m"
BMAG      = "\033[1;35m"
BCYN      = "\033[1;36m"
BWHT      = "\033[1;37m"
UBLK      = "\033[4;30m"
URED      = "\033[4;31m"
UGRN      = "\033[4;32m"
UYEL      = "\033[4;33m"
UBLU      = "\033[4;34m"
UMAG      = "\033[4;35m"
UCYN      = "\033[4;36m"
UWHT      = "\033[4;37m"
BLKB      = "\033[40m"
REDB      = "\033[41m"
GRNB      = "\033[42m"
YELB      = "\033[43m"
BLUB      = "\033[44m"
MAGB      = "\033[45m"
CYNB      = "\033[46m"
WHTB      = "\033[47m"
BLKHB     = "\033[0;100m"
REDHB     = "\033[0;101m"
GRNHB     = "\033[0;102m"
YELHB     = "\033[0;103m"
BLUHB     = "\033[0;104m"
MAGHB     = "\033[0;105m"
CYNHB     = "\033[0;106m"
WHTHB     = "\033[0;107m"
HBLK      = "\033[0;90m"
HRED      = "\033[0;91m"
HGRN      = "\033[0;92m"
HYEL      = "\033[0;93m"
HBLU      = "\033[0;94m"
HMAG      = "\033[0;95m"
HCYN      = "\033[0;96m"
HWHT      = "\033[0;97m"
BHBLK     = "\033[1;90m"
BHRED     = "\033[1;91m"
BHGRN     = "\033[1;92m"
BHYEL     = "\033[1;93m"
BHBLU     = "\033[1;94m"
BHMAG     = "\033[1;95m"
BHCYN     = "\033[1;96m"
BHWHT     = "\033[1;97m"
defualt = "\033[39m"


def banner(filename):
    with open(filename,"r",encoding="utf-8") as F:
        print(F.read())

def clear(clear_hex):
    print(clear_hex)


def system():
    uname = platform.uname()
    color(BLU)
    print(f"|System              |-> {uname.system}")
    print(f"|Node Name           |-> {uname.node}")
    print(f"|Release             |-> {uname.release}")
    print(f"|Version             |-> {uname.version}")
    print(f"|Machine             |-> {uname.machine}")
    print(f"|Processor           |-> {uname.processor}")
    color(YEL)
    print("|Physical CPU Cores  |-> ",psutil.cpu_count(logical=False))
    print("|Total CPU Cores     |-> ",psutil.cpu_count(logical=True))
    color(defualt)


def CFMMAIN():
    cpufreq = psutil.cpu_freq()
    print("CPU USAGE PER CORE")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        print(f"")

def CFM():
    cpufreq = psutil.cpu_freq()
    CPIFF = PrettyTable(['CPU USAGE PER CORE'])
    cpfi = psutil.cpu_percent(percpu=True, interval=1)
    CPIFF.add_row([
        cpfi
    ])
    print(cpfi)

def time():
    date_table = PrettyTable(['Date/Time Running/boot'])
    Datenow = str(datetime.now())
    date_table.add_row([Datenow])
    print(date_table)

def tab_macPT2():
    I_mac = get_mac_address(interface="eth1")
    eth_mac = get_mac_address(interface="docker0")
    eth2_mac = get_mac_address(interface="vmnet8")
    eth1_mac = get_mac_address(interface="vmnet1")
    Ii_mac = get_mac_address(interface="eth0")
    eth11_mac = get_mac_address(interface="wlan0")
    eth21_mac = get_mac_address(interface="wlan2")
    eth91_mac = get_mac_address(interface="wlan1")
    eth911_mac = get_mac_address(interface="lo")
    Mac_table = PrettyTable(["Mac Addresses Tied To Interface"])
    Mac_table.add_row([I_mac])
    Mac_table.add_row([eth_mac])
    Mac_table.add_row([eth2_mac])
    Mac_table.add_row([eth1_mac])
    Mac_table.add_row([Ii_mac])
    Mac_table.add_row([eth11_mac])
    Mac_table.add_row([eth21_mac])
    Mac_table.add_row([eth91_mac])
    Mac_table.add_row([eth911_mac])
    print(Mac_table)    


def arp():
    from getmac import getmac
    getmac.PORT = 55555
    IPNET = getmac.get_mac_address(ip="10.0.0.1", network_request=True)
    tab = PrettyTable(['Network Mac'])
    tab.add_row([IPNET])
    print(tab)



def getHwAddr(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', bytes(ifname, 'utf-8')[:15]))
    return ':'.join('%02x' % b for b in info[18:24])


def main():
    A = getHwAddr('eth0')
    C = getHwAddr('wlan0')
    D = getHwAddr('wlan2')
    E = getHwAddr('wlan1')
    F = getHwAddr('eth1')
    table_mac2 = PrettyTable(['Macs In Range'])
    table_mac2.add_row([A])
    table_mac2.add_row([C])
    table_mac2.add_row([D])
    table_mac2.add_row([E])
    table_mac2.add_row([F])
    print(table_mac2)


def main_main():
    while True:
        ch = "\x1b[H\x1b[2J\x1b[3J"
        clear(ch)
        banner("test.txt")
        system()
        table = PrettyTable(['Network', 'Status', 'Speed'])
        for key in psutil.net_if_stats().keys():
            name = key
            up = "Up" if psutil.net_if_stats()[key].isup else "Down"
            speed = psutil.net_if_stats()[key].speed
            table.add_row([name, up, speed])
        print(table)
        memory_table = PrettyTable(["Total", "Used", "Available", "Percentage"])
        vm = psutil.virtual_memory()
        memory_table.add_row([
            vm.total,
            vm.used,
            vm.available,
            vm.percent
        ])
        print(memory_table)
        process_table = PrettyTable(['PID', 'PNAME', 'STATUS',
                                    'CPU', 'NUM THREADS'])
        
        for process in psutil.pids()[-10:]:
            try:
                p = psutil.Process(process)
                process_table.add_row([
                    str(process),
                    p.name(),
                    p.status(),
                    str(p.cpu_percent())+"%",
                    p.num_threads()
                    ])
                
            except Exception as e:
                pass
        print(process_table)
        tab_macPT2()
        t.sleep(1)

if __name__ == "__main__":
    main_main()
