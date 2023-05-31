# PicoW
Four main files:
- Node1.py
- Node2.py
- server.py
- data.csv

Attached are three python scripts. Please fill out the wifi information in the server.py file. And upload server.py into both Nodes.

The Node1.py is for the central hub that will be receiving data.
The Node2.py is for the pico with two temperature probes attached.

Node2 prints out signal strength, and sends temp1 and temp2 data to Node1, which is continuously on the lookout for incoming data.
