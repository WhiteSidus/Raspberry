import machine
import time

led = machine.Pin(0, machine.Pin.OUT)
led2 = machine.Pin(1, machine.Pin.OUT)
led3 = machine.Pin(2, machine.Pin.OUT)
led4 = machine.Pin(3, machine.Pin.OUT)

leds = [led, led2, led3, led4]

def LightOption(Pin, option, delay):
    time.sleep(delay)
    return Pin.value(option)

while True:
    for led in leds:
        LightOption(led, 1, 1)
    for led in leds:
        LightOption(led, 0, 0)

