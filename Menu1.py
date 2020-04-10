#!/usr/bin/python
## Show menu ##
import os
import sys

print (30 * '-')
print ("   M A I N - M E N U")
print (30 * '-')
print ("1. CAM_Overflow Attack")
print ("2. ARP_Spoofing Attack (MiTM)")
print ("3. Reboot the server")
print (30 * '-')

## Choix de L'utilisateur ###
choice = input('Enter your choice [1-3] : ')

### Conversion du choix UT ##
choice = int(choice)

### Action en fonction du choix de l'UT ###
if choice == 1:
        print ("Starting CAM_Overflow Attack")
        exec(open("CAM_Overflow.py").read())
elif choice == 2:
        interface = input("Renseigne ton interface:\n")
        print ("Starting ARP_Spoofing Attack")
       ## subprocess.call(['ARP_spoofing.py', 'interface', '192.168.1.62' , '192.168.1.1' '1'])
        os.system("python ARP_Spoofing.py {interface} 192.168.1.62 192.168.1.1 1")
else:    ## default ##
        print ("Invalid number. Try again...")