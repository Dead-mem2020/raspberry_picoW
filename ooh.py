import machine
import time
import dht
 
sensor = dht.DHT11(machine.Pin(1)) 

led1 = machine.Pin(4, machine.Pin.OUT)
led2 = machine.Pin(3, machine.Pin.OUT)

while True:
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    print(f"Temperature: {temp}°C   Humidity: {hum}% ")
    if temp <= 22:  
        led1.on() #nezapomenout na ty závorky
        led2.off()
        time.sleep(1)

    elif temp >= 23:
        led1.on()
        led2.on()
        time.sleep(1)