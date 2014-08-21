'''
Created on Aug 21, 2014

@author: mzfa
'''
import pyaardvark as pyaa

if __name__ == '__main__':
    device = pyaa.find_devices()
    a = pyaa.open(port=device[0])
    print a.unique_id_str()