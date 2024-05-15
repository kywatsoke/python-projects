#!/usr/bin/env python

# Importing subprocess library
import subprocess

#Asking the user for the interface card and new MAC Address
interface = input("Enter the Network Interface : ")
new_mac_address = input("Enter the New MAC Address : ")

#Printing the output info
print("[+] Changing MAC Address for " + interface + " to " + new_mac_address)

# Using subprocess .run function to run the comment
subprocess.run("ifconfig " + interface + " down", shell=True)
subprocess.run("ifconfig " + interface + " hw ether " + new_mac_address, shell=True)
subprocess.run("ifconfig " + interface + " up", shell=True)

#Program End
#Day_001
#Learn_Python




