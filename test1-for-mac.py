#!/usr/bin/env python3

# metod for change mac-addres
import subprocess

# metod for --help and argument for linux terminal
import optparse

# function for new MAC-address
def change_mac(interface, new_mac):
    # method for input user
    # method 1
    print("[+] Change Mac address for " + interface + " to " + new_mac)
    # method 2
    subprocess.call(['ifconfig', interface, "down"])
    subprocess.call(['ifconfig', interface, "hw", "ether", new_mac])
    subprocess.call(['ifconfig', interface, "up"])

# use optparse
parser = optparse.OptionParser()

# commands for argiment
parser.add_option("-i", "--interface", dest="interface", help="Change name MAC address")
parser.add_option("-m", "--mac", dest="new_mac", help="Change MAC address")

# parser argument users, where options for users and arguments(comannds)
(options, arguments) = parser.parse_args()

# use func change_mac
change_mac(options.interface, options.new_mac)

# method for input user

# method 1
# interface = input("interface > ")
# new_mac = input("new MAC > ")
# print("[+] Change Mac address for " + interface + " to " + new_mac)

# method 2
# interface = options.interface
# new_mac = options.new_mac
# print("[+] Change Mac address for " + interface + " to " + new_mac)

# method 1
# subprocess.call("ifconfig " + interface + " down", shell=True)
# subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
# subprocess.call("ifconfig " + interface + " up", shell=True)

# method 2
# subprocess.call(['ifconfig', interface, "down"])
# subprocess.call(['ifconfig', interface, "hw", "ether", new_mac])
# subprocess.call(['ifconfig', interface, "up"])