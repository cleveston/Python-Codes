import socket
import platform
import os
import sys
import struct
import time
import select
import binascii

ICMP_ECHO_REQUEST = 8

def checksum(str):
    csum = 0
    countTo = (len(str) / 2) * 2
    
    count = 0

    while count < countTo:
        thisVal = ord(str[count+1]) * 256 + ord(str[count])
        csum = csum + thisVal
        csum = csum & 0xffffffffL
        count = count + 2


    if countTo < len(str):
        csum = csum + ord(str[len(str) - 1])
        csum = csum & 0xffffffffL

    csum = (csum >> 16) + (csum & 0xffff)
    csum = csum + (csum >> 16)
    answer = ~csum
    answer = answer & 0xffff
    answer = answer >> 8 | (answer << 8 & 0xff00)
    
    return answer


def receiveOnePing(mySocket, ID, timeout, destAddr):
    
    timeLeft = timeout

    while 1:
        startedSelect = time.time()
        whatReady = select.select([mySocket], [], [], timeLeft)
        howLongInSelect = (time.time() - startedSelect)

        if whatReady[0] == []: # Timeout
            return "Request timed out."

        timeReceived = time.time()
        recPacket, addr = mySocket.recvfrom(1024)

        ipHeader = recPacket[:20]
        ipVer, servType, length, ipID, ipFlagsOff, ipTTL, ipProc, ipChecksum, ipSrc, ipDest = struct.unpack("BBHHHBBHII", ipHeader)
        
        # Fetch the ICMP header from the IP packet
        icmpHeader = recPacket[20:28]
        icmpType, code, checksum, packID, sequence = struct.unpack("bbHHh", icmpHeader)
       
        if packID == ID:
            timeSent = struct.unpack("d", recPacket[28:28 + struct.calcsize("d")])[0]
            
            # Print out reply information
            delayMS = (timeReceived - timeSent)*1000
            packetSize = len(recPacket)
           
            if (delayMS < 1):
                print "Reply from " + destAddr + ": bytes=" + str(packetSize) + " time<=1ms TTL=" + str(ipTTL)
            else:
                print "Reply from " + destAddr + ": bytes=" + str(packetSize) + " time=" + str(int(round(delayMS,1))) + "ms TTL=" + str(ipTTL)
                
            return delayMS
      
        timeLeft = timeLeft - howLongInSelect
        
        if timeLeft <= 0:
            return "Request timed out."


def sendOnePing(mySocket, destAddr, ID):

    # Header is type (8), code (8), checksum (16), id (16), sequence (16)
    myChecksum = 0
    
    # Make a dummy header with a 0 checksum.
    # struct -- Interpret strings as packed binary data
    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1)
    data = struct.pack("d", time.time())
    
    # Calculate the checksum on the data and the dummy header.
    myChecksum = checksum(header + data)

    # Get the right checksum, and put in the header
    if sys.platform == 'darwin':
        myChecksum = socket.htons(myChecksum) & 0xffff

        #Convert 16-bit integers from host to network byte order.
    else:
        myChecksum = socket.htons(myChecksum)

    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1)
    packet = header + data
        
    mySocket.sendto(packet, (destAddr, 1)) # AF_INET address must be tuple, not str
    
    #Both LISTS and TUPLES consist of a number of objects
    #which can be referenced by their position number within the object
def doOnePing(destAddr, timeout, pignum):
    
    icmp = socket.getprotobyname("icmp")
    
    #SOCK_RAW is a powerful socket type. For more details see:http://sock-raw.org/papers/sock_raw
    icmpSocket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)

    myID = os.getpid() & 0xFFFF
    
    #Return the current process i
    sendOnePing(icmpSocket, destAddr, myID)
    delay = receiveOnePing(icmpSocket, myID, timeout, destAddr)
    icmpSocket.close()
    return delay


def ping(host, timeout=1, pings=4):
    delay = []
    minRTT = 1000000
    maxRTT = -1
    sumRTT = 0
    lost = 0
    
    # Get name of remote host
    dest = socket.gethostbyname(host)

    #Send ping requests to a server separated by <timeout> second
    for i in range(0, pings):
        delay.append(doOnePing(dest, timeout, i))
        time.sleep(1)

    # Calculate ping statistics
    for i in range(0, pings):
        if (delay[i] == -1):
            lost = lost + 1
        else:
            if (delay[i] < minRTT):
                minRTT = delay[i]
            if (delay[i] > maxRTT):
                maxRTT = delay[i]
            sumRTT = sumRTT + delay[i]

    lostPercent = (float(lost) / pings) * 100
    receivedPings = pings - lost
    averageRTT = sumRTT / pings

    print ""
    print "Packet statistics for " + dest + ":"
    print "\tSent = " + str(pings) + " Received = " + str(receivedPings) + " Lost = " + str(lost) + " (" + str(lostPercent) + "% loss)"
    if (lostPercent < 100):
        print "Round trip times in milliseconds:"
        print "\tMinimum=" + str(round(minRTT, 1)) + "ms Maximum=" + str(round(maxRTT, 1)) + "ms Average=" + str(round(averageRTT, 1)) + "ms"

#ping("www.google.com") #America
#ping("www1.cnnic.cn") #Asia
#ping("www.gov.uk") #Europe
ping("www.egypt.gov.eg") #Africa
print ""