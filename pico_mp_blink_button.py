import machine
import utime

led = machine.Pin("LED", machine.Pin.OUT)
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)

SLOW = 1.0
FAST = 0.1
DEBOUNCE_MS = 25

def pressed():
    if btn.value():
        return False
    utime.sleep_ms(DEBOUNCE_MS)
    return btn.value() == 0

while True:
    delay = FAST if pressed() else SLOW
    led.value(1)
    utime.sleep(delay)
    led.value(0)
    utime.sleep(delay)