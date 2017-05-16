#!/usr/bin/env python

# server.py 
import socket, datetime, pytz

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           
port = 50000

# bind to the port
serversocket.bind((host, port))                                  

# queue up to 5 requests
serversocket.listen(5)                                           

print("Waiting for connection...")

while True:
    # establish a connection
    clientsocket,addr = serversocket.accept()    
    print("\nGot a connection from %s " % str(addr))
    
    print("Waiting for timezone...")
    tz = clientsocket.recv(1024)
    
    if tz == 'close':
	print("Bye!")
	clientsocket.sendall('\r\n')
	serversocket.close()	
	break

    if tz not in pytz.all_timezones:
        print("Try again!")
	clientsocket.sendall("Sorry, not a valid timezone!\r\n")
	continue
    
    timezone = "The time in "+tz+" got from the server is "+str(datetime.datetime.now(pytz.timezone(tz)))+"!\r\n"
    clientsocket.sendall(timezone) 
    print("Done!")
    clientsocket.close()
    


