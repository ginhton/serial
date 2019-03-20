import serial
import binascii
t = serial.Serial('/dev/ttyUSB0', 115200)


sendComm = 'fc 05 03 01 47 4f 1a'
hex = bytes.fromhex(sendComm)


def P():
    while(True):
        t.read(1)
        t.read(t.inWaiting())
        t.write(hex)

P();
