import machine
import dht
import time
 
sensor = dht.DHT11(machine.Pin(0))  # Nastav pin 14 pro DHT11
 
while True:
    sensor.measure()  # Spusť měření
    print("Temperature:", sensor.temperature(), "°C")
    print("Humidity:", sensor.humidity(), "%")
    time.sleep(2)  # Pauza mezi měřeními

