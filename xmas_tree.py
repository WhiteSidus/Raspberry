import machine 
import time 

Out0 = machine.Pin(0, machine.Pin.OUT)
Out1 = machine.Pin(1, machine.Pin.OUT)
Out2 = machine.Pin(3, machine.Pin.OUT)

while True:
    Out0.value(1)
    time.sleep(0.5)
    Out0.value(0)

    Out1.value(1)
    time.sleep(0.5)
    Out1.value(0)

    Out2.value(1)
    time.sleep(0.5)
    Out2.value(0)