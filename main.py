import machine
import dht
import time

sensor = dht.DHT11(machine.Pin(0))           
buzzer = machine.Pin(1, machine.Pin.OUT)      
led1 = machine.Pin(2, machine.Pin.OUT)        
led2 = machine.Pin(3, machine.Pin.OUT)        
led3 = machine.Pin(4, machine.Pin.OUT)        
led4 = machine.Pin(5, machine.Pin.OUT)

button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    sensor.measure()  
    temperature = sensor.temperature()

    if button.value() == 0:
        print("Temperature:", temperature, "oC")
    else:
        print("Humidity:", sensor.humidity(), "%")

    if temperature < 20:
        led1.on()
        led2.off()
        led3.off()
        led4.off()
    elif 20 <= temperature < 25:
        led1.off()
        led2.on()
        led3.off()
        led4.off()
    elif 25 <= temperature < 30:
        led1.off()
        led2.off()
        led3.on()
        led4.off()
    else:  
        led1.off()
        led2.off()
        led3.off()
        led4.on()
    
    buzzer.on()
    time.sleep(0.01)
    buzzer.off()

    time.sleep(15)