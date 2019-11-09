#!/usr/bin/env python3

#This sample demonstrates turning relays on and off.
#Install Relay uHAT library with "pip3 install turta-relayuhat"

from time import sleep
from turta_relayuhat import Turta_Relay

#Initialize
relay = Turta_Relay.RelayController()

try:
    while 1:
        #Turn on relay 1
        relay.write(1, True)
        print("Relay 1 state: " + ("On" if relay.read(1) else "Off"))
        sleep(2.0)

        #Turn on relay 2
        relay.write(2, True)
        print("Relay 2 state: " + ("On" if relay.read(2) else "Off"))
        sleep(2.0)

        #Turn off relay 1
        relay.write(1, False)
        print("Relay 1 state: " + ("On" if relay.read(1) else "Off"))
        sleep(2.0)

        #Turn off relay 2
        relay.write(2, False)
        print("Relay 2 state: " + ("On" if relay.read(2) else "Off"))
        sleep(2.0)

        #Turn on all relays
        relay.write_all(True)
        print("Turn on all relays")
        sleep(2.0)

        #Turn off all relays
        relay.write_all(False)
        print("Turn off all relays")
        sleep(2.0)

except KeyboardInterrupt:
    print('Bye.')