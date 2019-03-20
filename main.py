import serial
import binascii
t = serial.Serial('/dev/ttyUSB0', 115200)

hexStr = bytes.fromhex('FE 01 01 FF')

num = t.write(hexStr);
print(num);
n = t.inWaiting();
data = str(binascii.b2a_hex(t.read(2)))
print(data)
