# Turta Relay uHAT Helper for Raspbian.
# Distributed under the terms of the MIT license.

# Python Library for relays.
# Version 1.0.0
# Released: November 9th, 2019

# Visit https://docs.turta.io for documentation.

import RPi.GPIO as GPIO

class RelayController:
    """Relay Controller"""

    #Variables
    is_initialized = False

    #Pins
    relay1, relay2 = 21, 22

    #Initialize
    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.relay1, GPIO.OUT)
        GPIO.setup(self.relay2, GPIO.OUT)
        GPIO.output(self.relay1, GPIO.LOW)
        GPIO.output(self.relay2, GPIO.LOW)
        self.is_initialized = True
        return

    #Relay Write Methods

    def write(self, ch, st):
        """Controls the relay.

        Parameters:
        ch (byte): Relay channel (1 to 2)
        st (bool): Relay state (True or False)"""

        if (ch == 1):
            GPIO.output(self.relay1, GPIO.HIGH if st else GPIO.LOW)
        elif (ch == 2):
            GPIO.output(self.relay2, GPIO.HIGH if st else GPIO.LOW)
        return

    def write_all(self, st):
        """Turns on or off all the relays.

        Parameters:
        st (bool): Relay states (True or False)"""

        GPIO.output(self.relay1, GPIO.HIGH if st else GPIO.LOW)
        GPIO.output(self.relay2, GPIO.HIGH if st else GPIO.LOW)
        return

    def toggle(self, ch):
        """Inverts the relay's state.

        Parameters:
        ch (byte): Relay channel (1 to 2)"""

        if (ch == 1):
            GPIO.output(self.relay1, GPIO.LOW if GPIO.input(self.relay1) else GPIO.HIGH)
        elif (ch == 2):
            GPIO.output(self.relay2, GPIO.LOW if GPIO.input(self.relay2) else GPIO.HIGH)
        return

    def toggle_all(self):
        """Inverts all the relay states."""

        GPIO.output(self.relay1, GPIO.LOW if GPIO.input(self.relay1) else GPIO.HIGH)
        GPIO.output(self.relay2, GPIO.LOW if GPIO.input(self.relay2) else GPIO.HIGH)
        return

    #Relay Read Methods

    def read(self, ch):
        """Reads the relay state.

        Parameters:
        ch (byte): Relay channel (1 to 2)

        Returns:
        bool: Relay state (True of False)"""

        if (ch == 1):
            return GPIO.input(self.relay1)
        elif (ch == 2):
            return GPIO.input(self.relay2)

    #Disposal
    def __del__(self):
        """Releases the resources."""
        if self.is_initialized:
            GPIO.output(self.relay1, GPIO.LOW)
            GPIO.output(self.relay2, GPIO.LOW)
            GPIO.cleanup()
            del self.is_initialized
        return
