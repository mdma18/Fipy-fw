#!/usr/bin/env python
import time
import pycom
# from network import Bluetooth
from lib.BluetoothLE import Blues
from lib.Sleep import Sleep
# from lib.HTTPS import HTTPS
from network import WLAN

pycom.heartbeat(False)

mSleep = Sleep()
while True:
    mSleep.Start()
# mBL = Blues()
# wlan = WLAN()
# wlan.init(mode=WLAN.AP, ssid="MDMA")

# while 1:
# print(wlan.ifconfig(id=1))
# mSleep.Start()
# print("Just sleeping..")
# time.sleep(1.00)
# print("Hello")
# mBL = Blues()
# mBL.ConnectBluetooth()
# mSleep = Sleep()
# mSleep.Start()
# mHTTPS = HTTPS()
# mHTTPS.Initialize()
