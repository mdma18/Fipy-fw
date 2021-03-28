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

    def __init__(self):
        print('Advertising Bluetooth...')
        self.mBluetooth = Bluetooth()
        self.mEvents = self.mBluetooth.events()
        # self.mBluetooth.init([id=0, mode=Bluetooth.BLE, antenna=Bluetooth.INT_ANT, modem_sleep=False, pin=None, privacy=True, secure_connections=True, mtu=200])
        self.mBluetooth.set_advertisement(
            name='FiPy', service_uuid=b'1804000000000000')
        self.mBluetooth.callback(trigger=self.mBluetooth.CLIENT_CONNECTED |
                                 self.mBluetooth.CLIENT_DISCONNECTED, handler=self.Connection)
        self.mBluetooth.advertise(True)
        self.CreateServChar()
        self.mCharacteristic.callback(
            trigger=self.mBluetooth.CHAR_READ_EVENT, handler=self.CharCallback)

    def Connect(self):
        self.mBluetooth.start_scan(-1)
        while True:
            mAdv = self.mBluetooth.get_adv()
            if mAdv:
                print(ubinascii.hexlify(mAdv.mac))

    def Connection(self, zResponse):
        self.mEvents = zResponse.events()
        if self.mEvents & self.mBluetooth.CLIENT_CONNECTED:
            print("Client connected")
        elif self.mEvents & self.mBluetooth.CLIENT_DISCONNECTED:
            print("Client disconnected")

    def CreateServChar(self):
        # Create service and characteristic
        self.mService = self.mBluetooth.service(
            uuid='0000000000000000', isprimary=True)
        self.mCharacteristic = self.mService.characteristic(uuid='0000000000000002', properties=self.mBluetooth.PROP_INDICATE |
                                                            self.mBluetooth.PROP_BROADCAST | self.mBluetooth.PROP_READ | self.mBluetooth.PROP_NOTIFY, value='InitialValue')

    def CharCallback(self, sChr):
        self.mEvents = sChr.events()
        if self.mEvents & self.mBluetooth.CHAR_READ_EVENT:
            print('Bluetooth.CHAR_READ_EVENT')

# def ConnectBluetooth(cls):
#         mBluetooth = Bluetooth()
#         mBluetooth.start_scan(-1)
#         # mBluetooth.set_advertisement(
#         #     name='Fipy', service_uuid=b'1234567890123456')
#         # mBluetooth.advertise(True)

#         # srv1 = mBluetooth.service(uuid=b'1234567890123456', isprimary=True)
#         # chr1 = srv1.characteristic(uuid=b'ab34567890123456', value=5)

#         mAdv = None
#         while True:
#             mAdv = mBluetooth.get_adv()
#             # print(mAdv)
#             if mAdv:
#                 print("Connected to device with addr = {}".format(
#                     ubinascii.hexlify(mAdv.mac)))
#         # services = mBluetooth.connect(mAdv.mac).services()
#         # print(services)
#         # for service in services:
#         #     print(service.uuid())
#         #     # try to get the complete name
#         #     print(mBluetooth.resolve_adv_data(
#         #         mAdv.data, Bluetooth.ADV_NAME_CMPL))

#         #     # try to get the manufacturer data (Apple's iBeacon data is sent here)
#         #     # mfg_data = mBluetooth.resolve_adv_data(
#         #     #     mAdv.data, Bluetooth.ADV_MANUFACTURER_DATA)

#         #     # if mfg_data:
#         #     #     # try to get the manufacturer data (Apple's iBeacon data is sent here)
#         #     #     print(binascii.hexlify(mfg_data))


#         #     if mBluetooth.resolve_adv_data(mAdv.data, Bluetooth.ADV_NAME_CMPL) == 'MDMA':
#         #         conn = mBluetooth.connect(mAdv.mac)
#         #         services = conn.services()
#         #         # print("Here")
#         #         for service in services:
#         #             time.sleep(0.050)
#         #             if type(service.uuid()) == bytes:
#         #                 print('Reading chars from service = {}'.format(
#         #                     service.uuid()))
#         #             else:
#         #                 print('Reading chars from service = %x' %
#         #                       service.uuid())
#         #             chars = service.characteristics()
#         #             for char in chars:
#         #                 if (char.properties() & Bluetooth.PROP_READ):
#         #                     print('char {} value = {}'.format(
#         #                         char.uuid(), char.read()))
#         #         conn.disconnect()
#         #         break
#             else:
#                 time.sleep(2.00)
