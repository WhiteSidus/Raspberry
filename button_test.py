import machine
import time

button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    if button.value() == 0:
        print("Button is Pressed")
    else:
        print("Button is not Pressed")
    time.sleep(0.3)