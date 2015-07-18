#wanglongtao

#houyufan
import socket,sys

#port = 11111
host = sys.argv[1]

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
	s.connect((host,port))
except socket.gaierror,e:
	print "Error connecting to server : %s" % e
	sys.exit(1)
	
	
s.sendall('hello server' + "\r\n")

while 1:
	buf = s.recv(2048)
	if not len(buf):
		break
	sys.stdout.write(buf)
	
