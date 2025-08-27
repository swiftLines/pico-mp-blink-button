import machine
import utime

# Create a Pin object for the onboard LED (set as an OUTPUT pin)
led1 = machine.Pin("LED", machine.Pin.OUT)

led2= machine.Pin(28, machine.Pin.OUT)
# Create a Pin object for a push button on GPIO 14 configured as an INPUT pin
# Set default state to High
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)

# Define fast and slow blink speeds
SLOW = 1.0  # 1 second delay
FAST = 0.1  # 0.1 second delay
DEBOUNCE_MS = 25  # 25 ms debounce time to avoid false button presses

# Function to check if the button is pressed
def pressed():
    if btn.value():  # Button is not pressed if value is High (1)
        return False
    utime.sleep_ms(DEBOUNCE_MS)  # Delay to filter out mechanical bouncing
    return btn.value() == 0  # Return True if button is Low (pressed)


def set_alternate(state):
    """Drive LEDs in opposit states: 0 -> led1 on, 1 -> led2 on."""
    led1.value(0 if state else 1)
    led2.value(1 if state else 0)


# Main program loop
state = 0  #toggles 0/1 each cycle
while True:
    # If button is pressed, blink LED fast; otherwise blink slow
    delay = FAST if pressed() else SLOW
    state ^= 1  # flip 0 <->1 each iteration
    set_alternate(state) # light one LED and turn the other off
    utime.sleep(delay)


    # led1.value(state)
    # led2.value(1 - state)
    # utime.sleep(delay)


    # # Turn LED on
    # led1.value(1)
    # utime.sleep(delay) # Wait for delay time
    # # Turn LED off
    # led1.value(0)
    # utime.sleep(delay) # Wait for delay time