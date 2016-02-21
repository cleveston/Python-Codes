from socket import *
import base64
import ssl

msg = '\r\n I love computer networks!'.encode('utf-8')

endmsg = '\r\n.\r\n'.encode('utf-8')

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = 'smtp.gmail.com'

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)

#Create SSL conection
ssl_clientSocket = ssl.wrap_socket(clientSocket) 
ssl_clientSocket.connect((mailserver, 465))

recv = ssl_clientSocket.recv(1024)

print(recv)

# Send HELO command and print server response.
heloCommand = 'HELO\r\n'.encode('utf-8')
ssl_clientSocket.send(heloCommand)
recv1 = ssl_clientSocket.recv(1024)
print(recv1)

#Initializa TLS
startTLScommand = 'STARTTLS\r\n'.encode('utf-8')
ssl_clientSocket.send(startTLScommand)
recvdiscard = ssl_clientSocket.recv(1024)
print(recvdiscard)
    
# Send AUTH command and print server response.
authCommand = 'AUTH LOGIN\r\n'.encode('utf-8')
ssl_clientSocket.send(authCommand)
recv1 = ssl_clientSocket.recv(1024)
print(recv1)

# Send LOGIN command and print server response.
loginCommand = base64.b64encode('iurycl@gmail.com'.encode('utf-8'))
loginCommand = loginCommand + '\r\n'.encode('utf-8')
ssl_clientSocket.send(loginCommand)
recv1 = ssl_clientSocket.recv(1024)
print(recv1)

# Send PASSWORD command and print server response.
passwordCommand = base64.b64encode('nodigasnadaparaninguem'.encode('utf-8'))
passwordCommand = passwordCommand + '\r\n'.encode('utf-8')
ssl_clientSocket.send(passwordCommand)
recv1 = ssl_clientSocket.recv(1024)
print(recv1)

# Send MAIL FROM command and print server response.
mailFromCommand = 'MAIL FROM: <iurycl@gmail.com>\r\n'.encode('utf-8')
ssl_clientSocket.send(mailFromCommand)
recv2 = ssl_clientSocket.recv(1024)
print(recv2)

# Send RCPT TO command and print server response.
rcptToCommand = 'RCPT TO: <iurycl@gmail.com>\r\n'.encode('utf-8')
ssl_clientSocket.send(rcptToCommand)
recv3 = ssl_clientSocket.recv(1024)
print(recv3)

# Send DATA command and print server response.
dataCommand = 'DATA\r\n'.encode('utf-8')
ssl_clientSocket.send(dataCommand)
recv4 = ssl_clientSocket.recv(1024)
print(recv4)

# Send message data.
ssl_clientSocket.send(msg)
# Message ends with a single period.
ssl_clientSocket.send(endmsg)

# Send QUIT command and get server response.
quitCommand = 'QUIT\r\n'.encode('utf-8')
ssl_clientSocket.send(quitCommand)
recv5 = ssl_clientSocket.recv(1024)
print(recv5)