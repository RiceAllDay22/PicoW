# PicoW
Four main files:
- Node1.py
- Node2.py
- server.py
- data.csv

The Node1.py is for the Pi Pico W that is designated as the central hub. It continuously listens for incoming data in the network and saves the data into the data.csv file.

The Node2.py is for the Pi Pico W with two temperature probes attached. It continuously prints out the wifi signal strength and sends temp1 and temp2 data to the central hub.

The server.py contains wifi information. It must be filled out appropriately and uploaded into both Nodes.
