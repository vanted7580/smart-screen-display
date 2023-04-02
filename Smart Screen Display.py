from time import sleep

import win32api
import ctypes
from ctypes import wintypes
import configparser

CONFIG_NAME = 'C:\ProgramData\Smart Screen Display\Smart Screen Display.ini'

config = configparser.ConfigParser()
screen = {
    'dc': 60,
    'ac': 240
}
config['screen'] = screen


def load_conf():
    if len(config.read(CONFIG_NAME)) == 0:
        with open(CONFIG_NAME, 'w') as configfile:
            config.write(configfile)
    config.read(CONFIG_NAME)
    return


class SYSTEM_POWER_STATUS(ctypes.Structure):
    _fields_ = [
        ('ACLineStatus', wintypes.BYTE)
    ]


def change_display_frequency(frequency):
    dm = win32api.EnumDisplaySettings(None, 0)
    dm.DisplayFrequency = frequency
    win32api.ChangeDisplaySettings(dm, 0)


def get_power_status():
    GetSystemPowerStatus = ctypes.windll.kernel32.GetSystemPowerStatus
    GetSystemPowerStatus.argtypes = [ctypes.POINTER(SYSTEM_POWER_STATUS)]
    GetSystemPowerStatus.restype = wintypes.BOOL

    status = SYSTEM_POWER_STATUS()
    if not GetSystemPowerStatus(ctypes.pointer(status)):
        return 1
    return status.ACLineStatus


load_conf()
target_rate = {
    0: screen['dc'],
    1: screen['ac']
}

sleep(0.5)

change_display_frequency(target_rate[get_power_status()])
