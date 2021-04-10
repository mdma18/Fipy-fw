#!/usr/bin/env python
import time
import pycom
import machine
from pysense.MPL3115A2 import MPL3115A2, ALTITUDE, PRESSURE
from pysense.LTR329ALS01 import LTR329ALS01
from pysense.SI7006A20 import SI7006A20
from pysense.LIS2HH12 import LIS2HH12
from pysense.pycoproc import Pycoproc


class Sleep:
    def __init__(self):
        self.py = Pycoproc(Pycoproc.PYSENSE)

    def WakeUp(self):

        print("Wakeup reason: " + str(self.py.get_wake_reason()) +
              "; Aproximate sleep remaining: " + str(self.py.get_sleep_remaining()) + " sec")
        time.sleep(0.5)

        # enable wakeup source from INT pin
        self.py.setup_int_pin_wake_up(False)

        # Enable interrupts from accelerometer (P13) and button (P14)  JMCD:  bug report, only use one of these lines, subsequent calls overwrite earlier setup
        # machine.pin_sleep_wakeup(
        #     ['P13'], mode=machine.WAKEUP_ANY_HIGH, enable_pull=False)

        # enable activity and also inactivity interrupts, using the default callback handler
        self.py.setup_int_wake_up(True, True)

        acc = LIS2HH12()
        # enable the activity/inactivity interrupts
        # set the accelereation threshold to 2000mG (2G) and the min duration to 200ms
        acc.enable_activity_interrupt(2000, 200)

        # check if we were awaken due to activity
        if acc.activity():
            print("Awoken due to activity")
            pycom.rgbled(0xFF0000)
        else:
            pycom.rgbled(0x00FF00)  # timer wake-up
        time.sleep(0.1)

        # go to sleep for 5 minutes maximum if no accelerometer interrupt happens
        self.py.setup_sleep(5)
        self.py.go_to_sleep()

    def Example(self):

        py = Pycoproc(Pycoproc.PYSENSE)

        # Returns height in meters. Mode may also be set to PRESSURE, returning a value in Pascals
        mp = MPL3115A2(py, mode=ALTITUDE)
        print("MPL3115A2 temperature: " + str(mp.temperature()))
        print("Altitude: " + str(mp.altitude()))
        # Returns pressure in Pa. Mode may also be set to ALTITUDE, returning a value in meters
        mpp = MPL3115A2(py, mode=PRESSURE)
        print("Pressure: " + str(mpp.pressure()))

        si = SI7006A20(py)
        print("Temperature: " + str(si.temperature()) +
              " deg C and Relative Humidity: " + str(si.humidity()) + " %RH")
        print("Dew point: " + str(si.dew_point()) + " deg C")
        t_ambient = 24.4
        print("Humidity Ambient for " + str(t_ambient) +
              " deg C is " + str(si.humid_ambient(t_ambient)) + "%RH")

        lt = LTR329ALS01(py)
        print("Light (channel Blue lux, channel Red lux): " + str(lt.light()))

        li = LIS2HH12(py)
        print("Acceleration: " + str(li.acceleration()))
        print("Roll: " + str(li.roll()))
        print("Pitch: " + str(li.pitch()))

        print("Battery voltage: " + str(py.read_battery_voltage()))

        time.sleep(3)
        # py.setup_sleep(10)
        # py.go_to_sleep()
