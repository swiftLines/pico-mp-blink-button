import machine
import utime

# --- Pins ---
# Create a Pin object for the onboard LED (set as an OUTPUT pin)
led1 = machine.Pin("LED", machine.Pin.OUT)
# External LED on GP28
led2= machine.Pin(28, machine.Pin.OUT)
# Create a Pin object for a push button on GPIO 14 configured as an INPUT pin
# Set default state to High
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)

# --- Timing constants
SLOW = 1.0  # 1 second delay
FAST = 0.1  # 0.1 second delay
DEBOUNCE_MS = 25  # 25 ms debounce time to avoid false button presses


def pressed():
    """
    Return True once per click.
    Debounce on the press, then wait for release before returning True.
    """
    if btn.value() == 0:  # Detect press (active low)
        utime.sleep_ms(DEBOUNCE_MS)  # Settle contacts
        if btn.value() == 0:  # Still pressed?
            # Wait for release so toggle is now repeated while held
            while btn.value() == 0:  
                utime.sleep_ms(1)
            return True
    return False


def set_alternate(state):
    """Drive LEDs in opposit states: 0 -> led1 on, 1 -> led2 on."""
    led1.value(0 if state else 1)
    led2.value(1 if state else 0)


# Main program loop
mode_fast = False  # False=SLOW, True=FAST
state = 0  # Toggles 0/1 each cycle

while True:
    if pressed():
        mode_fast = not mode_fast  # Flip speed mode on each click

    delay = FAST if mode_fast else SLOW
    # Alternate LEDs
    state ^= 1
    set_alternate(state)
    utime.sleep(delay)
    