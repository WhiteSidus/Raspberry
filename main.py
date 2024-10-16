import machine
import time

led = machine.Pin(0, machine.Pin.OUT)
led2 = machine.Pin(1, machine.Pin.OUT)
led3 = machine.Pin(2, machine.Pin.OUT)
led4 = machine.Pin(3, machine.Pin.OUT)

a = True

while a:
    led.value(1)
    time.sleep(0.5)  
    led.value(0)
    time.sleep(0.5)
    
    led2.value(1)
    time.sleep(0.5)  
    led2.value(0)
    time.sleep(0.5)

    led3.value(1)
    time.sleep(0.5)  
    led3.value(0)
    time.sleep(0.5)

    led4.value(1)
    time.sleep(0.5)  
    led4.value(0)
    time.sleep(0.5)

    led.value(1)
    time.sleep(0.5)
    led2.value(1)
    time.sleep(0.5)
    led3.value(1)
    time.sleep(0.5)
    led4.value(1)

    led.value(0)
    time.sleep(0.5)
    led2.value(0)
    time.sleep(0.5)
    led3.value(0)
    time.sleep(0.5)
    led4.value(0)