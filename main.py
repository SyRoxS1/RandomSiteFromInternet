import subprocess
import socket 


def ping(ip): #response = 1 means host respond to ping
    res = subprocess.call(['ping', '-n', '1', ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    return res

def portscan(adress,port): #response = 1 means port open
    socket.setdefaulttimeout(1) 
    tcp_socket =socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
    result = tcp_socket.connect_ex((adress,int(port)))
    tcp_socket.close()
    return result

ip_test = '192.3.155.223'

if ping(ip_test) == 0: 
    hostup = True
    print("OK") 

else:
    hostup = False
    print("NO")



print(portscan("192.3.155.223","0"))

