import serial
import binascii
import timeit
from time import sleep

def Hex(command, n):
    hexStr = bytes.fromhex(command)
    num = t.write(hexStr);
    data = t.read(1)
    data += t.read(t.inWaiting());
    return data

t = serial.Serial('/dev/ttyUSB0', 115200)

data = Hex('fe 09 10 46 16 dc 1b 00 4b 12 00 ff', 3)

print(str(binascii.b2a_hex(data)))
