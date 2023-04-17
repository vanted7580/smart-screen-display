import win32api
import ctypes
from ctypes import wintypes


target_rate = {
    0: 60,
    1: 240
}


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

change_display_frequency(target_rate[get_power_status()])
