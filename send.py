import serial
import binascii
import timeit
from time import sleep
t = serial.Serial('/dev/ttyUSB0', 115200)

def Hex(command, n):
    hexStr = bytes.fromhex(command)
    num = t.write(hexStr);
    data = t.read(1)
    data += t.read(t.inWaiting());
    return data

# addr = '8a d9'
# sendComm = 'fc 05 03 01 '+addr+' 00'
sendComm = 'fc 05 03 01 8a d9 00'
hex = bytes.fromhex(sendComm)


def P():
    t0 = timeit.default_timer()
    t.write(hex)
    data = t.read(1)
    t.read(t.inWaiting())
    elapsed = timeit.default_timer() - t0
    print(data)
    print(elapsed);
    sleep(1);


# t = repeat('P()', 'from __main__ import P', number=3, repeat=4);
# print(t);
P();
# while(True):
#     P();

# data = Hex('fe 09 10 46 16 dc 1b 00 4b 12 00 ff', 3)

# print(str(binascii.b2a_hex(data)))
