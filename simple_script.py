from config import GET_WHOLE_COLOR_KEYBOARD_BUFFER, KEYS,GET_COLOR_PACKET, GET_COLOR_PACKET_START, GET_BRIGHTNESS_PACKETS
from KspHid import KspHidHelper, KspHid


#Get not splitted keyboard buffer
KEYBOARD_BUFFER = GET_WHOLE_COLOR_KEYBOARD_BUFFER()


#Set WSAD keys to green
KEYBOARD_BUFFER.replace_at_offset(GET_COLOR_PACKET(0,255,0), KEYS['W'])
KEYBOARD_BUFFER.replace_at_offset(GET_COLOR_PACKET(0,255,0), KEYS['S'])
KEYBOARD_BUFFER.replace_at_offset(GET_COLOR_PACKET(0,255,0), KEYS['A'])
KEYBOARD_BUFFER.replace_at_offset(GET_COLOR_PACKET(0,255,0), KEYS['D'])


#Create instruction protocol (to be added later to the packets)
START_COLOR_PACKET = GET_COLOR_PACKET_START()

#Get keyboard path
usb_path = KspHidHelper.get_interface_path_for_pidvid(0x0951, 0x16e5, 3)

#Initialise usb
kb = KspHid(usb_path)

#Create packets to set brightness to 50%
BRIGHTNESS_TO_SEND_PACKETS = GET_BRIGHTNESS_PACKETS(128)
for packet in BRIGHTNESS_TO_SEND_PACKETS:
    kb.execute_packet_buffer(packet.get(), True)

while True:
    COLOR_TO_SEND_PACKETS = [START_COLOR_PACKET] + KEYBOARD_BUFFER.split_into_buffers(64)
    for packet in COLOR_TO_SEND_PACKETS:
        kb.execute_packet_buffer(packet.get(), True)
    
    

    



