# dB2ms

import math

def dB2ms(dBps):
    ms = 20 / (dBps * math.log(10)) * 10**3
    return ms

while True:
    dBps_value = float(input("Enter dB/s value: "))
    ms_value = dB2ms(dBps_value)
    print(f"{dBps_value} dB/s is equal to {ms_value:.2f} ms.")
