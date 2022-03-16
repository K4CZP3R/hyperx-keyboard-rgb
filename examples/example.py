from hyperx_keyboard_rgb.models.ksp_keyboard import KspKeyboard
from hyperx_keyboard_rgb.helpers.hyperx_alloy_origins import COLOR_KEYBOARD_BUFFER, COLOR_KEY, KEYS, COLOR_KEYBOARD_PACKETS

hid_path = input("Path:")


# Define keyboard
keyboard = KspKeyboard(hid_path.encode("ASCII"))
try:
    keyboard.connect()
except Exception as e:
    print("Can't connect!", e)
    exit(1)


# Setup keyboard colors
keyboard_buffer = COLOR_KEYBOARD_BUFFER()
for i in ['K', 'S', 'P']:
    keyboard_buffer.replace_at_offset(COLOR_KEY(255, 0, 0), KEYS[i])

try:
    while True:
        for packet in COLOR_KEYBOARD_PACKETS(keyboard_buffer):
            keyboard.send_feature_report(packet.get(), True)
except KeyboardInterrupt:
    exit()
