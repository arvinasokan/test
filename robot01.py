import socket 
import sys


import videostream

ip_addr='127.0.0.1'
###############################################################################

host0=''
port0=50000

try:
  s0 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error, msg0 :
  print 'Failed to create socket. Error Code : ' + str(msg0[0]) + ' Message ' + msg0[1]
  sys.exit()
###############################################################################

host1=''
port1=50001

try:
  a1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error, msg1 :
  print 'Failed to create socket. Error Code : ' + str(msg1[0]) + ' Message ' + msg1[1]
  sys.exit()
print 'sending ack 1'
a1.sendto('ack',(ip_addr,50001))

while 1:
  x=1
  y=videostream.videostream()
  s0.sendto(y,(ip_addr,50000))
  print 'robot : sent sensor data 0'
  d1 = a1.recvfrom(6144)
  actuatordata1 = d1[0]
  actuatoraddr1 = d1[1]
  #videostream.applicationlayer(actuatordata1)
  print 'robot : received actuator data 1'

