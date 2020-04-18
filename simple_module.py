from config import GET_WHOLE_COLOR_KEYBOARD_BUFFER, GET_COLOR_PACKET_START, GET_COLOR_PACKET, KEYS, GET_BRIGHTNESS_PACKETS
from KspHid import KspHid, KspHidHelper

class ProofOfConcept():
    def __init__(self):
        self.kb = KspHid(KspHidHelper.get_interface_path_for_pidvid(0x0951, 0x16e5, 3))
        self.KEYBOARD_BUFFER = GET_WHOLE_COLOR_KEYBOARD_BUFFER()
    
    def send_colors_to_keyboard(self):
        COLOR_TO_SEND_PACKETS = [GET_COLOR_PACKET_START()] + self.KEYBOARD_BUFFER.split_into_buffers(64)
        for packet in COLOR_TO_SEND_PACKETS:
            self.kb.execute_packet_buffer(packet.get(), True)
    
    def set_keys_to_color(self, keys, r,g,b):
        for key in keys:
            self.KEYBOARD_BUFFER.replace_at_offset(GET_COLOR_PACKET(r,g,b), KEYS[key])

    def set_brightness(self, new_value):
        for packet in GET_BRIGHTNESS_PACKETS(new_value):
            self.kb.execute_packet_buffer(packet.get(), True)


poc = ProofOfConcept()

poc.set_keys_to_color(['W','S','A','D'], 255,0,0)
poc.set_keys_to_color(['N_7', 'N_9'], 0,0,255)
poc.set_keys_to_color(['N_5'], 255,255,0)
poc.set_keys_to_color(['N_1','N_0','N_DOT','N_3'], 255,0,0)


poc.send_colors_to_keyboard()
