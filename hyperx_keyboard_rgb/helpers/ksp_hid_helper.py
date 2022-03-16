import hid
from models.ksp_hid_device import KspHidDevice
from typing import List


class KspHidHelper():
    @staticmethod
    def get_devices() -> List[KspHidDevice]:
        """Get all available HID devices, and sort them

        Returns:
            List[KspHidDevice]: All available devices
        """
        enumerated = hid.enumerate()

        devices: List[KspHidDevice] = []

        for e_dict in enumerated:
            # check if subdevice of already existing device
            subdevice = False
            for device in devices:
                try:
                    device.add_subdevice(e_dict)
                    subdevice = True
                except ValueError:
                    continue

            if subdevice:
                continue

            devices.append(KspHidDevice(e_dict))
        return devices
