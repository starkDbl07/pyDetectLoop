#!/usr/bin/python

import sys
import socket
import struct
import binascii

#rawSocket=socket.socket(socket.PF_PACKET,socket.SOCK_RAW,socket.htons(0x0800))
rawSocket=socket.socket(socket.PF_PACKET,socket.SOCK_RAW)
rawSocket.bind(("eth1", 0x0806))

while True:
	packet=rawSocket.recv(1024)

	eth_header=packet[0:12]
	eth_data = struct.unpack("!6s6s", eth_header)
	dest_mac = binascii.hexlify(eth_data[0])
	src_mac = binascii.hexlify(eth_data[1])
	print src_mac
	if src_mac == "005056263fc5":
		print "loop detected"
		sys.exit(1)
