'''
Created on Aug 21, 2014

@author: mzfa
'''
import pyaardvark

if __name__ == '__main__':
    device = pyaardvark.find_devices()
    a = pyaardvark.open(port=device[0])
    id_str = a.unique_id_str()
#     array = []
#     for i in range(256):
#         array.append("0")
#     a.i2c_bitrate = 400
    data = ''.join('%c' % c for c in 'abcde')
    print data
    a.i2c_master_write(0x53, data)
    a.poll(20)
    data1 = a.i2c_master_read(0x53, 256)
    print data1
    print(' '.join('%02x' % ord(c) for c in data1))
    a.close()
#     print id_str,"closed"