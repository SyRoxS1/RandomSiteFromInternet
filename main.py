import subprocess
import socket 
import sys
import requests
import random
import threading
from multiprocessing.dummy import Pool as ThreadPool

import threading

from multiprocessing import Process

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
        return r.status_code
    else:
        return False
def checkResponseCode(code):
    if code >= 100 and code <= 199:
        return "informational"
    if code >= 200 and code <= 299:
        return "successful"
    if code >= 300 and code <= 399:
        return "redirection"
    if code >= 400 and code <= 499:
        return "client error"
    if code >= 500 and code <= 599:
        return "server error"
    
    
def randomIP():
    a = random.randint(0,255)
    b = random.randint(0,255)
    c = random.randint(0,255)
    d = random.randint(0,255)
    return(str(a)+'.'+str(b)+'.'+str(c)+'.'+str(d))





def start(ip):
    print("trying IP : "+str(ip))
    if portscan(ip,"80") == 0:
        print("port 80 open")
        A = requestHTTP(ip)
        if A != False:
            print("IP : "+ ip + " is up and running http server, code : " + str(A))
            with open("upip.txt","a") as f:
                f.write(ip + "\n")

        else:
            print("NO RESPOND FROM HTTP")




def run_start_with_threads(ip_addresses):
    threads = []
    for ip in ip_addresses:
        thread = threading.Thread(target=start, args=(ip,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()
if __name__ == '__main__':
   with open("IPS", 'r') as file:
    # Read lines from the file and remove leading/trailing whitespaces
    ip_addresses = [line.strip() for line in file]

   run_start_with_threads(ip_addresses)