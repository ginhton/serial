import serial
t = serial.Serial('/dev/ttyUSB0', 115200)

str = 0xFE0101FF

n = t.write(str);
print 'start read'
str = t.read(n)
print 'end read'
print str
