# PICO NUMBER 1

# Built from: https://thepihut.com/blogs/raspberry-pi-tutorials/wireless-communication-between-two-raspberry-pi-pico-w-boards

# Import Libraries
import network
import socket
import time
from machine import Pin, ADC
from secret import ssid,password
import random 
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

# Wait for connect or fail
max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)

# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('connected')
    status = wlan.ifconfig()
    print( 'ip = ' + status[0] )

# Open socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)
print('listening on', addr)

# Main Loop: Listen for connections and incoming data
while True:
    try:
        cl, addr = s.accept()
        print('client connected from', addr)
        incoming = cl.recv(1024)
        print(incoming)
        cl.close()

    except OSError as e:
        #cl.close()
        print('connection closed')
    finally:
        cl.close()


