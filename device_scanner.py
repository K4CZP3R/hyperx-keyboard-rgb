from PyInquirer import prompt, print_json
from helpers.ksp_hid_helper import KspHidHelper

print("Getting all HID devices...")
devices = KspHidHelper.get_devices()

for device in devices:
    print(f"[*] {device}:")
    for sub in device.subdevices:
        print(">>>>", sub)