#!/usr/bin/env python
import pycom
# from lib.BL import Blues
from lib.Sleep import Sleep

pycom.heartbeat(False)

while 1:
    # print("Hello")
    # mBL = Blues()
    # mBL.ConnectBluetooth()
    mSleep = Sleep()
