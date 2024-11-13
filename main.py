import machine
import dht
import time

# Inicializace senzoru a pinů pro LED a buzzer
sensor = dht.DHT11(machine.Pin(0))           # DHT11 senzor na GPIO 0
buzzer = machine.Pin(1, machine.Pin.OUT)      # Buzzer na GPIO 1
led1 = machine.Pin(2, machine.Pin.OUT)        # LED1 na GPIO 2
led2 = machine.Pin(3, machine.Pin.OUT)        # LED2 na GPIO 3
led3 = machine.Pin(4, machine.Pin.OUT)        # LED3 na GPIO 4
led4 = machine.Pin(5, machine.Pin.OUT)        # LED4 na GPIO 5

while True:
    sensor.measure()  # Spustí měření
    temperature = sensor.temperature()
    print("Temperature:", temperature, "°C")
    print("Humidity:", sensor.humidity(), "%")
    
    # Rozsvícení LED podle teplotního rozsahu
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
    else:  # temperature >= 30
        led1.off()
        led2.off()
        led3.off()
        led4.on()
    
    # Zvuková indikace, že měření proběhlo
    buzzer.on()
    time.sleep(0.1)
    buzzer.off()

    # Pauza mezi měřeními
    time.sleep(5)