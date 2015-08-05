import socket,sys

host = sys.argv[1]
port = int(sys.argv[2])

print 'please input:'
mess = raw_input()
#input message

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#create a socket

try:
	s.connect((host,port))
	#connect to server
except socket.gaierror,e:
	print "Error connecting to server : %s" % e
	sys.exit(1)

print 'successfully connected!'

try:
	s.sendall(mess)
	s.shutdown(1)
	#send message
except (KeyboardInterrupt,SystemExit):
	raise
except:
	traceback.print_exc()

while 1:
	buf = s.recv(2048)
	if not len(buf):
		break
	sys.stdout.write(buf)
	#read message from server and print it
	
print 'connect stop!'
