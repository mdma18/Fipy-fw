#!/usr/bin/env python
#
# Copyright (c) 2019, Pycom Limited.
#
# This software is licensed under the GNU GPL version 3 or any
# later version, with permitted additional terms. For more information
# see the Pycom Licence v1.0 document supplied with this file, or
# available at https://www.pycom.io/opensource/licensing
#
import time
import ubinascii
from network import Bluetooth


class Blues:

    # Initialization method.
    def __init__(self):
        print('Advertising Bluetooth...')
        self.mBluetooth = Bluetooth()
        self.mEvents = self.mBluetooth.events()
        # self.mBluetooth.init([id=0, mode=Bluetooth.BLE, antenna=Bluetooth.INT_ANT, modem_sleep=False, pin=None, privacy=True, secure_connections=True, mtu=200])
        self.mBluetooth.set_advertisement(
            name='FiPy', service_uuid=2)
        self.mBluetooth.callback(trigger=self.mBluetooth.CLIENT_CONNECTED |
                                 self.mBluetooth.CLIENT_DISCONNECTED, handler=self.Connection)
        self.mBluetooth.advertise(True)
        # Create Service & Characteristic
        self.CreateServChar()
        self.mCharacteristic.callback(
            trigger=self.mBluetooth.CHAR_WRITE_EVENT | self.mBluetooth.CHAR_READ_EVENT, handler=self.CharCallback)

    # Connection method: Used as callback function to detect a BLE connection.
    def Connection(self, zResponse):
        self.mEvents = zResponse.events()
        if self.mEvents & self.mBluetooth.CLIENT_CONNECTED:
            print("Client connected")
        elif self.mEvents & self.mBluetooth.CLIENT_DISCONNECTED:
            print("Client disconnected")

    def CreateServChar(self):
        # Create service and characteristic
        self.mService = self.mBluetooth.service(
            uuid=3, isprimary=True)
        self.mCharacteristic = self.mService.characteristic(
            uuid=31, properties=self.mBluetooth.PROP_WRITE | self.mBluetooth.PROP_READ, value=6)

    def CharCallback(self, chr, zResponse):
        self.mEvents, value = zResponse
        if self.mEvents & self.mBluetooth.CHAR_READ_EVENT:
            print("Read from Char = {}".format(value))

        if self.mEvents & self.mBluetooth.CHAR_WRITE_EVENT:
            print("Written to Char = {}".format(value))

# mBluetooth.disconnect_client()
