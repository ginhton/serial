## serial
* code about a network project

* main target
  - get delay between end-node to coordinator

* main idea
  - A send data to B.  When B receive data, B will resend data to A immediately
  - A, B are end-node or coordinator

* main file
  - receive.py
  - send.py
  - getInfo.py

* other file **no use**

* prerequisite
  - install python3
  - install pip3
  - install pyserial throught pip3
  - device can connect to node successfully

* how to use (Under Linux)
  - clone this repository in coordinator-connected laptop and end-node-connected laptop
  - use `python3 getInfo.py` to get node's local short address
  - fill correct address in `send.py` and `receive.py`
  - establish nodes in both laptops
  - optional: establish some router 
  - run `python3 receive.py` firstly in one laptop, then `python3 send.py` the other
