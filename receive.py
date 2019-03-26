import serial
import binascii
from time import sleep
t = serial.Serial('/dev/ttyUSB0', 115200)


addr = '3f 29'
sendComm = 'fc 05 03 01 '+ addr +' 1a'
hex = bytes.fromhex(sendComm)


def P():
    t.read(1)
    t.read(t.inWaiting())
    print('read done')
    t.write(hex)
    print('write done')
    sleep(1.1)

P();

P();

P();

P();

