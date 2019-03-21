import serial
import binascii
import timeit
from time import sleep

loop = False

t = serial.Serial('/dev/ttyUSB0', 115200)

def Hex(command, n):
    hexStr = bytes.fromhex(command)
    num = t.write(hexStr);
    data = t.read(1)
    data += t.read(t.inWaiting());
    return data

addr = 'd9 af'
sendComm = 'fc 05 03 01 '+addr+' 00'
# sendComm = 'fc 05 03 01 98 35 00'
hex = bytes.fromhex(sendComm)


def P():
    t0 = timeit.default_timer()
    t.write(hex)
    data = t.read(1)
    t.read(t.inWaiting())
    elapsed = timeit.default_timer() - t0
    print(data)
    print(elapsed);
    sleep(1.2);


# t = repeat('P()', 'from __main__ import P', number=3, repeat=1);
# print(t);

P();

P();

P();

P();

