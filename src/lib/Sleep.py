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
    @classmethod
    def __init__(cls):
        pass

    @classmethod
    def Start(cls):

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
