#!/usr/bin/env python
#
# Copyright (c) 2019, Pycom Limited.
#
# This software is licensed under the GNU GPL version 3 or any
# later version, with permitted additional terms. For more information
# see the Pycom Licence v1.0 document supplied with this file, or
# available at https://www.pycom.io/opensource/licensing
#

import binascii
import time
from network import Bluetooth


class Blues:
    @classmethod
    def __init__(cls):
        pass

    @classmethod
    def ConnectBluetooth(cls):
        mBluetooth = Bluetooth()
        mBluetooth.start_scan(-1)
        while True:
            adv = mBluetooth.get_adv()
            if adv:
                # try to get the complete name
                print(mBluetooth.resolve_adv_data(
                    adv.data, Bluetooth.ADV_NAME_CMPL))

                # try to get the manufacturer data (Apple's iBeacon data is sent here)
                mfg_data = mBluetooth.resolve_adv_data(
                    adv.data, Bluetooth.ADV_MANUFACTURER_DATA)

                if mfg_data:
                    # try to get the manufacturer data (Apple's iBeacon data is sent here)
                    print(binascii.hexlify(mfg_data))

                if mBluetooth.resolve_adv_data(adv.data, Bluetooth.ADV_NAME_CMPL) == 'Heart Rate':
                    conn = mBluetooth.connect(adv.mac)
                    services = conn.services()

                    for service in services:
                        time.sleep(0.050)
                        if type(service.uuid()) == bytes:
                            print('Reading chars from service = {}'.format(
                                service.uuid()))
                        else:
                            print('Reading chars from service = %x' %
                                  service.uuid())
                        chars = service.characteristics()
                        for char in chars:
                            if (char.properties() & Bluetooth.PROP_READ):
                                print('char {} value = {}'.format(
                                    char.uuid(), char.read()))
                    conn.disconnect()
                    break
            else:
                time.sleep(0.050)

    @classmethod
    def Blah(cls):
        pass
