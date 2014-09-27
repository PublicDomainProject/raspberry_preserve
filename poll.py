#!/usr/bin/env python
# encoding: utf-8

import sys
import time

import Adafruit_DHT

def dformat():
    return "%Y-%m-%d %H:%M"

def poll():
    sensor = Adafruit_DHT.AM2302
    pin = 4
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    
    if humidity is not None and temperature is not None:
        return (humidity, temperature)
    else:
	    return None


def main(argv=None):
    
    p_result = None
    while p_result == None:
        p_result = poll()
    
    print "%s,%.2f,%.02f" % (time.strftime(dformat()), p_result[0], p_result[1])

	
if __name__ == "__main__":
	sys.exit(main())