'''
Created on Jun 17, 2014

@author: mzfa
'''
from clown import pyaardvark

if __name__ == '__main__':
    a = pyaardvark.Adapter(bitrate=100)
    a.open(portnum=0)
    print a.unique_id()
    a.read_reg(0x05)
#     a.write_reg(0x05, 1)
#     for i in range(1024):
#         a.read()
    a.close()