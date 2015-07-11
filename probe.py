#!/usr/bin/python

ETH_TYPE_ARP=0x0806

import socket
from struct import pack, unpack

ether_socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
ether_socket.bind(("eth1", ETH_TYPE_ARP))
ether_addr = ether_socket.getsockname()[4]

print ether_socket.getsockname()

ether_frame = [
	pack("!H", 0xffff),			#THA-1
	pack("!H", 0xffff),			#THA-2
	pack("!H", 0xffff),			#THA-3
	pack("!H", 0x0050),			#SHA-1
	pack("!H", 0x5626),			#SHA-2
	pack("!H", 0x3fc5),			#SHA-3
	pack("!h", ETH_TYPE_ARP),		#TYPE
	pack("!h", 1), 				#HTYPE
	pack("!h", 0x0800), 			#PTYPe
	pack("!B", 6),				#HLEN
	pack("!B", 4),				#PLEN
	pack("!h", 1),				#OPER
	pack("!H", 0x0050),			#SHA-1
	pack("!H", 0x5626),			#SHA-2
	pack("!H", 0x3fc5),			#SHA-3
	socket.inet_aton("172.17.255.190"),	#SPA
	pack("!H", 0xffff),			#THA-1
	pack("!H", 0xffff),			#THA-2
	pack("!H", 0xffff),			#THA-3
	socket.inet_aton("172.17.255.190"),	#SPA
	#socket.inet_aton("255.255.255.255"),	#TPA
]


print ether_frame
ether_socket.send(''.join(ether_frame))

ether_socket.close()
