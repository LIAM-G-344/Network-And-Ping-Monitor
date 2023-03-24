import os
import sys
import time
from configparser import ConfigParser
from pythonping import ping
import speedtest
from os import system, name
import socket

os.system("mode con cols=120 lines=20")

os.chdir(os.path.dirname(sys.argv[0]))


test = speedtest.Speedtest()

test.get_servers()
best = test.get_best_server()
print("Conecting To Server", end = ''), time.sleep(0.5), print(".", end = ''), time.sleep(0.5), print(".", end = ''), time.sleep(0.5), print(".", end = ''), time.sleep(0.5), print(".")
time.sleep(1)
print("Connected")

#this defines the clear() command
def clear():
  
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

print("-----------------------------------------------------------------------------------------------------------------------")
time.sleep(2)
print("Download Speed")
download_result = test.download()
download_mbs = round(download_result / (10**6), 2)
print(download_mbs, "Mb/s")

print("Upload Speed")
upload_result = test.upload()
upload_mbs = round(upload_result / (10**6), 2)
print(upload_mbs, "Mb/s")

parser = ConfigParser()
parser.read('adresses.ini')
p_1 = (parser.get('information_tracker', 'ping_1'))
p_2 = (parser.get('information_tracker', 'ping_2'))
p_3 = (parser.get('information_tracker', 'ping_3'))
p_4 = (parser.get('information_tracker', 'ping_4'))

print("                                                     Ping List")
print("-----------------------------------------------------------------------------------------------------------------------")
#p_1
print("Pinging:", p_1)
ip_list1 = [p_1]

for host in ip_list1:

    try:
        ip = socket.gethostbyname(host)
        result = ping(ip, count=1)
        if result.success():
            status_1 = ('online')

    except socket.error:
        status_1 = ('offline')

if status_1 == 'online':
    response_1 = ping(p_1, size=40, count=10, timeout=1000)
    print("Ping", response_1.rtt_avg_ms, "ms")
else:
    print(p_1,"Is Offline")
#p_2
print("Pinging:", p_2)
ip_list2 = [p_2]

for host in ip_list2:

    try:
        ip = socket.gethostbyname(host)
        result = ping(ip, count=1)
        if result.success():
            status_2 = ('online')

    except socket.error:
        status_2 = ('offline')

if status_2 == 'online':
    response_2 = ping(p_2, size=40, count=10, timeout=1000)
    print("Ping", response_2.rtt_avg_ms, "ms")
else:
    print(p_2, "Is Offline")
#p_3
print("Pinging:", p_3)
ip_list2 = [p_3]

for host in ip_list2:

    try:
        ip = socket.gethostbyname(host)
        result = ping(ip, count=1)
        if result.success():
            status_3 = ('online')

    except socket.error:
        status_3 = ('offline')

if status_3 == 'online':
    response_3 = ping(p_3, size=40, count=10, timeout=1000)
    print("Ping", response_3.rtt_avg_ms, "ms")
else:
    print(p_3, "Is Offline")
#p_4
print("Pinging:", p_4)
ip_list4 = [p_4]

for host in ip_list4:

    try:
        ip = socket.gethostbyname(host)
        result = ping(ip, count=1)
        if result.success():
            status_4 = ('online')

    except socket.error:
        status_4 = ('offline')

if status_4 == 'online':
    response_4 = ping(p_2, size=40, count=10, timeout=1000)
    print("Ping", response_4.rtt_avg_ms, "ms")
else:
    print(p_4, "Is Offline")

time.sleep(120)
clear()
#repeater

#repeater

rp_1 = 30

while rp_1 == 30:
    def clear():
  
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')
    print("-----------------------------------------------------------------------------------------------------------------------")
    time.sleep(2)
    print("Download Speed")
    print(download_mbs, "Mb/s")

    print("Upload Speed")
    print(upload_mbs, "Mb/s")

    parser = ConfigParser()
    parser.read('adresses.ini')
    p_1 = (parser.get('information_tracker', 'ping_1'))
    p_2 = (parser.get('information_tracker', 'ping_2'))
    p_3 = (parser.get('information_tracker', 'ping_3'))
    p_4 = (parser.get('information_tracker', 'ping_4'))

    print("                                                     Ping List")
    print("-----------------------------------------------------------------------------------------------------------------------")
    #p_1
    print("Pinging:", p_1)
    ip_list1 = [p_1]

    for host in ip_list1:

        try:
            ip = socket.gethostbyname(host)
            result = ping(ip, count=1)
            if result.success():
                status_1 = ('online')

        except socket.error:
            status_1 = ('offline')

    if status_1 == 'online':
        response_1 = ping(p_1, size=40, count=10, timeout=1000)
        print("Ping", response_1.rtt_avg_ms, "ms")
    else:
        print(p_1,"Is Offline")
    #p_2
    print("Pinging:", p_2)
    ip_list2 = [p_2]

    for host in ip_list2:

        try:
            ip = socket.gethostbyname(host)
            result = ping(ip, count=1)
            if result.success():
                status_2 = ('online')

        except socket.error:
            status_2 = ('offline')
    
    if status_2 == 'online':
        response_2 = ping(p_2, size=40, count=10, timeout=1000)
        print("Ping", response_2.rtt_avg_ms, "ms")
    else:
        print(p_2, "Is Offline")
    #p_3
    print("Pinging:", p_3)
    ip_list2 = [p_3]

    for host in ip_list2:

        try:
            ip = socket.gethostbyname(host)
            result = ping(ip, count=1)
            if result.success():
                status_3 = ('online')

        except socket.error:
            status_3 = ('offline')

    if status_3 == 'online':
        response_3 = ping(p_3, size=40, count=10, timeout=1000)
        print("Ping", response_3.rtt_avg_ms, "ms")
    else:
        print(p_3, "Is Offline")
    #p_4
    print("Pinging:", p_4)
    ip_list4 = [p_4]

    for host in ip_list4:

        try:
            ip = socket.gethostbyname(host)
            result = ping(ip, count=1)
            if result.success():
                status_4 = ('online')

        except socket.error:
            status_4 = ('offline')

    if status_4 == 'online':
        response_4 = ping(p_2, size=40, count=10, timeout=1000)
        print("Ping", response_4.rtt_avg_ms, "ms")
    else:
        print(p_4, "Is Offline")
    time.sleep(120)
    clear()
