# PICO NUMBER 1

# Built from: https://thepihut.com/blogs/raspberry-pi-tutorials/wireless-communication-between-two-raspberry-pi-pico-w-boards

# Import libraries
import network
import socket
import time
from secret import ssid, password
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

# Open file
file=open("data.csv","w")

# Main Loop: Listen for connections and incoming data
while True:
    try:
        # Retrieve data
        cl, addr = s.accept()
        incoming = cl.recv(1024)
        print(incoming)
        
        # Retrieve timestamp and write to file
        dt = time.localtime()  # (year, month, day, hour, minute, second, day of the week, day of the year
        timestamp = [dt[2], dt[3], dt[4], dt[5]]
        for i in range(0, len(timestamp)):
            file.write(str(timestamp[i]))
            file.write(",")
        file.write(incoming)
        file.write("\n")
        file.flush()
        cl.close()

    except OSError as e:
        cl.close()
        print('connection closed')
    finally:
        cl.close()
