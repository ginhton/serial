import serial
import binascii
t = serial.Serial('/dev/ttyUSB0', 115200)

# str = 0xFE0101FF
# hexStr = bytes.fromhex('FE 01 01 FF')

print(4)
# t.write(hexStr)
str = t.read(1)
print(str)
