'''
	udp socket client
	Silver Moon
	sender
'''

import socket	#for sockets
import sys	#for exit
from check import ip_checksum
# use it in this way
#https://www.bogotobogo.com/python/Multithread/python_multithreading_subclassing_Timer_Object.php
# create dgram udp socket

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
	print 'Failed to create socket'
	sys.exit()

host = 'localhost';
port = 8888;
seqnum = 0  # sequence number


while(1) :
	msg = raw_input('Enter message to send : ')

	chks = str(ip_checksum(msg))					#convert checksum return value to string
	data = (str(seqnum) + chks + msg)				#all 3 values are strings and merged together
	try :
		# Set the whole string
		# s.sendto(msg, (host, port))
		s.sendto(data, (host, port))

		# receive data from client (data, addr)
		d = s.recvfrom(1024)
		acknum = d[0]
		reply = d[1]
		addr = d[2]
		
		#check for ack
		if acknum == str(seqnum):
			print 'Good ack'
			if seqnum == 0:
				seqnum = 1
			else:
				seqnum = 0
		else:
			print 'Bad ack'
			s.sendto(data, (host, port))
			
			 
		print 'Server reply : ' + reply
	
	except socket.error, msg:
		print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
		sys.exit()
