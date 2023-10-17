# dBms

import math

def dB2ms(dBps):
    ms = 20 / (dBps * math.log(10)) * 10**3
    return ms
