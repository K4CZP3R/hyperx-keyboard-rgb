from time import sleep
from hyperx_keyboard_rgb.keyboard import KeyboardHelper, Keyboard
from hyperx_keyboard_rgb.exceptions.device_not_open import DeviceNotOpen
from hyperx_keyboard_rgb.helpers.hyperx_alloy_origins import KEYS
from hyperx_keyboard_rgb.models.ksp_color import KspColor


found_sub = KeyboardHelper.get_subdevice(0x951, 0x16e5, 0)

kb = Keyboard.from_ksp_hid_subdevice(found_sub)

try:
    kb.connect()
except DeviceNotOpen:
    print("Can't open device :(")
    exit(1)


kb.start_thread()
for key in KEYS.keys():
    kb.set_color(KEYS[key], KspColor(255, 0, 0))
    sleep(0.1)
