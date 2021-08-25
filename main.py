import socket
from IPy import IP
import threading


def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname()


def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        print("[+] Port" + str(port) + ' Is Open!')
    except:
        print("[+] Port" + str(port) + ' Is Closed!')


ipaddress = input('[+] Enter Target To Scan: ')
converted_ip = check_ip(ipaddress)

for port in range(75, 85):
    scan_port(converted_ip, port)

threads = []

for i in range(5):
    t = threading.Thread(target=scan_port(ipaddress, port))
    threads.append(t)

for i in range(5):
    threads[i].start()

for i in range(5):
    threads[i].join()
