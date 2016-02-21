#import socket module
from socket import *

HOST = '127.0.0.1'
PORT = 12345

#Create socket
serverSocket = socket(AF_INET, SOCK_STREAM)

#Try to bind socket to a port
try:
    serverSocket.bind((HOST, PORT))
    serverSocket.listen(5)
except Exception as msg:
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()
        
while True:
    #Establish the connection
    print('Ready to serve...')
    
    connectionSocket, addr = serverSocket.accept()
    
    try:
        message = connectionSocket.recv(1024)
        
        #Get the filename
        filename = message.split()[1]
        
        #Open file
        f = open(filename[1:]).read()
        
        #Send one HTTP header line into socket
        outputdata = 'HTTP/1.1 200 OK\r\n'
        outputdata += "Content-Type: text/html\r\n\r\n"
        
        outputdata += f

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode('utf-8'))
            
        #close client socket
        connectionSocket.close()
        
    except IOError:
        
        #Send response message for file not found
        outputdata = 'HTTP/1.1 404 Not Found\r\n'
        outputdata += "Content-Type: text/html\r\n\r\n"
            
         #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode('utf-8'))
        
        #Close client socket
        connectionSocket.close()

#Close server socket
serverSocket.close()

 
