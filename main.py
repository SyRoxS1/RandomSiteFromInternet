import subprocess
import socket 
import sys
import requests

def ping(ip): #response = 1 means host respond to ping
    res = subprocess.call(['ping', '-n', '1', ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    return res

def portscan(adress,port): #response = 1 means port open
    socket.setdefaulttimeout(1) 
    tcp_socket =socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
    result = tcp_socket.connect_ex((adress,int(port)))
    tcp_socket.close()
    return result

def scanAllPorts(ip):
    try:
        # will scan ports between 1 to 65,535
        for port in range(1,65535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            print("port : " + str(port))
            # returns an error indicator
            result = s.connect_ex((ip,port))
            if result ==0:
                print("Port {} is open".format(port))
            s.close()
             
    except KeyboardInterrupt:
            print("\n Exiting Program !!!!")
            sys.exit()
    

def requestHTTP(ip):
    try:
        r = requests.get('http://'+ip+'/')
        print(r.status_code)
    except:
        return False
    if r.status_code >= 200 and r.status_code <= 299:
        return True
    else:
        return False
    
ip_test = '192.58.214.244'


if ping(ip_test) == 0: 
    hostup = True
    print("OK") 

else:
    hostup = False
    print("NO")





for i in range(255):
    ip = "172.217.20." + str(i)
    print("scanning ip : " + ip)
    if portscan(ip,"80") == 0:
        print("IP : "+ ip + " is up doing http request ...")
        requestHTTP(ip)
        if requestHTTP(ip) == True:
            print("IP : "+ ip + " is up and running http server")
        else:
            print("not up")

    else:
        print("IP : "+ ip + " is down")



print(requestHTTP("178.32.155.237"))
