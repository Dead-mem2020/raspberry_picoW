import machine
import time

led1 = machine.Pin(1, machine.Pin.OUT)
led2 = machine.Pin(2, machine.Pin.OUT)
led3 = machine.Pin(3, machine.Pin.OUT)
led4 = machine.Pin(4, machine.Pin.OUT)


def LightOption(Pin, option, delay):
    time.sleep(delay)
    return Pin.value(option)

leds = [led1, led2, led3, led4]

while True:
    for led in leds:
        LightOption(led, 1, 1)
    time.sleep(1)
    for led in leds:
        LightOption(led, 0, 0)