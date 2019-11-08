'''
	Simple udp socket server
	reciever
'''

import socket
import sys

HOST = ''	# Symbolic name meaning all available interfaces
PORT = 8888	# Arbitrary non-privileged port
ack = 0

# Datagram (udp) socket
try :
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	print 'Socket created'
except socket.error, msg :
	print 'Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
	sys.exit()


# Bind socket to local host and port
try:
	s.bind((HOST, PORT))
except socket.error , msg:
	print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
	sys.exit()
	
print 'Socket bind complete'

#now keep talking with the client
while 1:
	# receive data from client (data, addr)
	d = s.recvfrom(1024)		# Need to pull the seqnum and the checksum value
	seqnum = d[0]
	chks = d[1:3]
	data = d[3]
	addr = d[4]
	
	if not data: 
		break
	elif seqnum == str(acknum):
		print 'Ack Good'
		rchks = str(ip_checksum(data))		# may need d[3:]
		if chks == rchks:
			print 'Sum Good'
			reply = 'OK...' + str(acknum) + data
			s.sendto(reply , addr)
		else:
			print 'Sum Bad'
		if acknum == 0:						# MAY need to move this assignment
			acknum = 1
		else:
			acknum = 0
	else:
		print 'Ack Bad'
		reply = 'OK...' + data
		s.sendto(reply , addr)
	#reply = 'OK...' + data
	#s.sendto(reply , addr)
	print 'Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.strip()
	
s.close()
