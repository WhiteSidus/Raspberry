import machine

led = machine.Pin(0, machine.Pin.OUT)
key = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    if not key.value():
        led.high
    else:
        led.low