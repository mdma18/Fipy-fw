#!/usr/bin/env python
import time
import pycom
# from network import Bluetooth
from lib.BL import Blues
# from lib.Sleep import Sleep
# from lib.HTTPS import HTTPS

pycom.heartbeat(False)


mBL = Blues()

while 1:
    print("Just sleeping..")
    time.sleep(1.00)
# print("Hello")
# mBL = Blues()
# mBL.ConnectBluetooth()
# mSleep = Sleep()
# mSleep.Start()
# mHTTPS = HTTPS()
# mHTTPS.Initialize()
