#Import Libraries
import socket
from time import sleep

#Colors
White = "\033[1;97m"
Grean = "\033[1;92m"
Yellow = "\033[1;93m"
Red = "\033[1;91m"

try:
 def WebIp():
#Input Target
  Target = input('\033[1;91m\nEnter Target: ' + White)
#Get Ip From Website (Function In Socket)
  IP = socket.gethostbyname(Target)
  sleep(0.5)
  Ld = print("\n Loading.")
  sleep(1)
  Ld = print(" Loading..")
  sleep(1)
  Ld = print(" Loading...\n")
  sleep(2)

  print("\033[1;93mTarget: " +Grean +Target)
  print("\033[1;93mIP: " + Grean +IP)
#Import Definition
 WebIp()

except:
 print("\033[1;91m\nPlease Try Again.. !!")
 WebIp()
