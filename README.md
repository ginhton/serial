<h2><center>serial</center></h2>
code about a network project

## Main Target
  get delay between end-node and coordinator

## Main Idea
* A send data to B.  When B receive data, B will resend data to A immediately
* A, B are end-node or coordinator

## Main Files
* receive.py
* send.py
* getInfo.py

* PS: other files are **no use**

## Prerequisite
* install python3
* install pip3
* install pyserial throught pip3
* device can connect to node successfully

## How to Use (Under Linux)
* clone this repository in coordinator-connected laptop and end-node-connected laptop
* use `python3 getInfo.py` to get node's local short address
* fill correct address in `send.py` and `receive.py`
* establish nodes in both laptops
* optional: establish some router 
* run `python3 receive.py` firstly in one laptop, then `python3 send.py` the other
