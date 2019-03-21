import serial
import binascii
import timeit
from time import sleep

def Hex(command):
    hexStr = bytes.fromhex(command)
    num = t.write(hexStr);
    data = t.read(1)
    data += t.read(t.inWaiting());
    return data

# command
commands = [
    'fe 01 02 ff', # network status
    'fe 01 05 ff', # local network short address
    'fe 01 06 ff', # local MAC address
    'fe 09 10 mac_addr ff' # get short address for specific mac address
]

t = serial.Serial('/dev/ttyUSB0', 115200)

# sample end node address
# data = Hex('fe 09 10 46 16 dc 1b 00 4b 12 00 ff')
data = Hex(commands[1])

print(str(binascii.b2a_hex(data)))
