import machine
import utime

# Create a Pin object for the onboard LED (set as an OUTPUT pin)
led = machine.Pin("LED", machine.Pin.OUT)
# Create a Pin object for a push button on GPIO 14 configured as an INPUT pin
# Set default state to High
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)

# Define fast and slow blink speeds
SLOW = 1.0  # 1 second delay
FAST = 0.1  # 0.1 second delay
DEBOUNCE_MS = 25. # 25 ms debounce time to avoid false button presses

# Function to check if the button is pressed
def pressed():
    if btn.value():  # Button is not pressed if value is High (1)
        return False
    utime.sleep_ms(DEBOUNCE_MS)  # Delay to filter out mechanical bouncing
    return btn.value() == 0  # Return True if button is Low (pressed)

# Main program loop
while True:
    # If button is pressed, blink LED fast; otherwise blink slow
    delay = FAST if pressed() else SLOW
    # Turn LED on
    led.value(1)
    utime.sleep(delay) # Wait for delay time
    # Turn LED off
    led.value(0)
    utime.sleep(delay) # Wait for delay time