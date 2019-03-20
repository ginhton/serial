import serial
import binascii

Command = [
    {},

    { 'command': 'fe 01 01 ff', 'mean': 'device type', 'length': 2, result: {0: 'xietiaoqi', 1: 'router', 2: 'node'}},
    { 'command': 'fe 01 02 ff', 'mean': 'network status', 'length': 2, result: {0: 'xietiaoqi', 1: 'router', 2: 'node'}},
    { 'command': 'fe 01 03 ff', 'mean': 'pan id', 'length': 3, result: {0: 'xietiaoqi', 1: 'router', 2: 'node'}},
    { 'command': 'fe 01 04 ff', 'mean': 'network key', 'length': 17, result: {0: 'xietiaoqi', 1: 'router', 2: 'node'}},
    { 'command': 'fe 01 05 ff', 'mean': 'localhost network short address', 'length': 3, result: {0: 'xietiaoqi', 1: 'router', 2: 'node'}},

    { 'command': 'fe 01 06 ff', 'mean': 'localhost mac address', 'length': 9, result: {0: 'xietiaoqi', 1: 'router', 2: 'node'}},
    { 'command': 'fe 01 07 ff', 'mean': 'coor short address', 'length': 3, result: {0: 'xietiaoqi', 1: 'router', 2: 'node'}},
    { 'command': 'fe 01 08 ff', 'mean': 'coor mac address', 'length': 9, result: {0: 'xietiaoqi', 1: 'router', 2: 'node'}},
    { 'command': 'fe 01 09 ff', 'mean': 'group number', 'length': 2, result: {0: 'xietiaoqi', 1: 'router', 2: 'node'}},
    { 'command': 'fe 01 0a ff', 'mean': 'channel', 'length': 2, result: {0: 'xietiaoqi', 1: 'router', 2: 'node'}},

    { 'command': 'fe 01 0b ff', 'mean': 'tx power', 'length': 2, result: {0: 'xietiaoqi', 1: 'router', 2: 'node'}},
    { 'command': 'fe 01 0c ff', 'mean': 'baud', 'length': 2, result: {0: 'xietiaoqi', 1: 'router', 2: 'node'}},
    { 'command': 'fe 01 0d ff', 'mean': 'sleep time (end-node only)', 'length': 2, result: {0: 'xietiaoqi', 1: 'router', 2: 'node'}},
    { 'command': 'fe 01 0e ff', 'mean': 'data-saving time', 'length': 2, result: {0: 'xietiaoqi', 1: 'router', 2: 'node'}},

    { 'command': 'fe 01 fe ff', 'mean': 'all info', 'length': 46, result: {0: 'xietiaoqi', 1: 'router', 2: 'node'}},

    { 'command': 'fe 09 10 mac_addr ff', 'mean': 'mac 2 short address', 'length': 3, result: {0: 'xietiaoqi', 1: 'router', 2: 'node'}},
    { 'command': 'fe 04 20 addr gpiox ff', 'mean': 'get gpio status', 'length': 7, result: {0: 'xietiaoqi', 1: 'router', 2: 'node'}},
    { 'command': 'fe 04 21  ff', 'mean': 'all info', 'length': 46, result: {0: 'xietiaoqi', 1: 'router', 2: 'node'}},
    { 'command': 'fe 01 fe ff', 'mean': 'all info', 'length': 46, result: {0: 'xietiaoqi', 1: 'router', 2: 'node'}},
    { 'command': 'fe 01 fe ff', 'mean': 'all info', 'length': 46, result: {0: 'xietiaoqi', 1: 'router', 2: 'node'}},
]

def Hex(command, n):
    hexStr = bytes.fromhex(command)
    num = t.write(hexStr);
    data = t.read(1)
    data += t.read(t.inWaiting());
    return data

if __name__ == "__main__":
    t = serial.Serial('/dev/ttyUSB0', 115200)
    print(Hex('fe 01 01 ff', 1))
