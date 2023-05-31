# PICO NUMBER 2

# Built from: https://thepihut.com/blogs/raspberry-pi-tutorials/wireless-communication-between-two-raspberry-pi-pico-w-boards

# Import Libraries
import network
import time
from secret import ssid, password, ip
import socket
import random
import onewire, ds18x20, time
from machine import Pin

# Setup temperature sensors
SensorPin = Pin(26, Pin.IN)
led = Pin("LED", Pin.OUT)
sensor = ds18x20.DS18X20(onewire.OneWire(SensorPin))
roms = sensor.scan()
sensor1 = roms[0]
sensor2 = roms[1]

# Connect to network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)
while not wlan.isconnected() and wlan.status() >= 0:
    print("Waiting to connect:")
    time.sleep(1)

# Should be connected and have an IP address
wlan.status() # 3 == success
wlan.ifconfig()
print(wlan.ifconfig())

# Main Loop: Send data to Node 1
while True:
    accessPoints = wlan.scan()
    for ap in accessPoints:
        if ap[0] == b'WhyWifiExpensive':
            print(f'strength = {ap[3]}')

    ai = socket.getaddrinfo(ip, 80) # Address of Web Server
    addr = ai[0][-1]

    # Create a socket and make a HTTP request
    s = socket.socket() # Open socket
    s.connect(addr)
    
    
    #Collect Data
    sensor.convert_temp()
    #dt = time.localtime()  # (year, month, day, hour, minute, second, day of the week, day of the year

    temp1 = int(round(sensor.read_temp(sensor1),1) *9/5 +32)
    temp2 = int(round(sensor.read_temp(sensor2),1) *9/5 +32)
    print('temp1:', temp1)
    print('temp2:', temp2)
    print('')
    
    data = str(temp1) + "," + str(temp2)
    
    s.send(data)
    s.close()          # Close socket
    time.sleep(2)      # wait

