import socket,traceback,sys

host = ''
port = int(sys.argv[1])

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#create a socket
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
#set options
s.bind((host,port))
#bind to host and port 
s.listen(1)
#set number of client waiting in the queue

while 1:
	try:
		clientsock,clientaddr = s.accept()
		#accept socket from client
	except KeyboardInterrupt:
		raise
	except:
		traceback.print_exc()
		continue

	try:
		print 'got connection from',clientsock.getpeername()
		#print client info
	except (KeyboardInterrupt,SystemExit):
		raise
	except:
		traceback.print_exc()

	try:
		fs = clientsock.makefile('rw',0)
		#create a file object
		print 'makefile()'
	except (KeyboardInterrupt,SystemExit):
		raise
	except:
		traceback.print_exc()

	try:
		mess = fs.readline().strip()
		print 'client wrote:',mess
		#get message from client
	except (KeyboardInterrupt,SystemExit):
		raise
	except:
		traceback.print_exc()

	try:
		fs.write('welcome' + str(clientsock.getpeername()) + '\n')
		fs.write('you have written:' + mess + '\n')
		fs.flush()
		#send message
	except (KeyboardInterrupt,SystemExit):
		raise
	except:
		traceback.print_exc()

	try:
		fs.close()
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
