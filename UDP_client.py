'''
	udp socket client
	Silver Moon
	sender
'''

import socket	#for sockets
import sys	#for exit
from check import ip_checksum
# use it in this way

# create dgram udp socket
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
	print 'Failed to create socket'
	sys.exit()

host = 'localhost';
port = 8888;
seqnum = "0"  # sequence number


while(1) :
	msg = raw_input('Enter message to send : ')

	chks = str(ip_checksum(msg))
	data = (seqnum + chks + msg)
	try :
		# Set the whole string
		# s.sendto(msg, (host, port))
		s.sendto(data, (host, port))

		# receive data from client (data, addr)
		d = s.recvfrom(1024)
		reply = d[0]
		addr = d[1]
		
		print 'Server reply : ' + reply
	
	except socket.error, msg:
		print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
		sys.exit()
