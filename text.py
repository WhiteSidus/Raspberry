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
show_temperature = True  # Výchozí režim

while True:
    if button.value() == 0:
        show_temperature = False
        time.sleep(0.02)

    sensor.measure()  
    temperature = sensor.temperature()

    if show_temperature:
        print("Temperature:", temperature, "°C")
    else:
        print("Humidity:", sensor.humidity(), "%")

    led1.value(temperature < 20)
    led2.value(20 <= temperature < 25)
    led3.value(25 <= temperature < 30)
    led4.value(temperature >= 30)
    
    # Aktivace buzzera na krátkou dobu
    buzzer.on()
    time.sleep(0.01)
    buzzer.off()

    # Pauza mezi iteracemi
    time.sleep(0.3)
