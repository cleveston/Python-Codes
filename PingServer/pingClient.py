import time
from socket import *

SERVER = "127.0.0.1"
TOTAL_PINGS = 10

successful = 0
totalTime = 0
rttMin = 0
rttMax = 0

#Send the pings to the server
for pings in range(TOTAL_PINGS):

    #UDP socket
    clientSocket = socket(AF_INET, SOCK_DGRAM)

    #Define the client server timeout
    clientSocket.settimeout(1)

    #Ping to server
    message = "Testing the response\n".encode('utf-8')

    addr = (SERVER, 12000)

    #Start the timer
    start = time.time()
    
    #Send the ping itself
    clientSocket.sendto(message, addr)

    #Try to receive the data em print the response
    try:
        data, server = clientSocket.recvfrom(1024)
        
        #Stop the timer
        end = time.time()
        
        #Calculates the elapsed time
        elapsed = end - start
        
        totalTime += elapsed
        
        #The first time
        if pings == 0:
            rttMin = elapsed
        
        #Verify the min and max times
        if elapsed > rttMax:
            rttMax = elapsed
        elif elapsed < rttMin:
            rttMin = elapsed   
        
        #Compose the response
        response = data.decode('utf-8') + " " + str(pings) + " " + str(elapsed) + "\n"
        
        print(response.encode('utf-8'))
        
        successful += 1

    #When timeout occurs, print the specific message
    except timeout:
        print("REQUEST TIMED OUT".encode('utf-8'))


result = "RTT Min: " + str(rttMin) 
print(result.encode('utf-8'))

result = "RTT Max: " + str(rttMax)
print(result.encode('utf-8'))

result = "RTT Average: " + str(totalTime/successful)
print(result.encode('utf-8'))

result = "Package Loss: " + str((TOTAL_PINGS - successful)*10) + "%"
print(result.encode('utf-8'))
