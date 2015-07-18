import socket,traceback,sys,time

host = ''
port = 11111

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((host,port))
s.listen(1)

while 1:
	try:
		clientsock,clientaddr = s.accept()
	except KeyboardInterrupt:
		raise
	except:
		traceback.print_exc()
		continue

	try:
		print 'got connection from',clientsock.getpeername()
		clientsock.sendall('hello\n')
	except (KeyboardInterrupt,SystemExit):
		raise
	except:
		traceback.print_exc()

	try:
		clientsock.close()
	except KeyboardInterrupt:
		raise
	except:
		traceback.print_exc()
