import serial
import binascii
t = serial.Serial('/dev/ttyUSB0', 115200)

# str = 0xFE0101FF
# hexStr = bytes.fromhex('FE 01 01 FF')
hexStr = 'FE0101FF'.decode("hex")

num = t.write(hexStr);
print(num);
n = t.inWaiting();
print('start read')
if n:
    data = str(binascii.b2a_hex(t.read(n)))
    print('end read')
    print(data)
