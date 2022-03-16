from typing import List
from hyperx_keyboard_rgb.models.ksp_packet import KspPacket
from hyperx_keyboard_rgb.models.ksp_color import KspColor

HYPERX_PACKET_BUFFER_SIZE = 64


def COLOR_KEYBOARD_START() -> KspPacket:
    """Packet which informs keyboard that the next packets will be color packets

    Returns:
        KspPacket: Packet with color instruction
    """
    p = KspPacket(HYPERX_PACKET_BUFFER_SIZE)
    p.replace_at_offset([0x04, 0xf2], 0)
    return p


def COLOR_KEYBOARD_BUFFER() -> KspPacket:
    """Buffer containing all key definitions. Every key has its own offset with length of (4)

    Returns:
        KspPacket: Buffer containing all key definitions
    """
    BUFFER_LEN = 64*9
    BUFFER = KspPacket(BUFFER_LEN)

    empty_packet = KspPacket(HYPERX_PACKET_BUFFER_SIZE)
    for i in range(0, HYPERX_PACKET_BUFFER_SIZE, 4):
        empty_packet.replace_at_offset(KspColor(0, 0, 0).get_instruction(), i)
    for i in range(0, BUFFER_LEN, 64):
        BUFFER.replace_at_offset(empty_packet.get_raw(), i)
    return BUFFER


def COLOR_KEYBOARD_PACKETS(color_keyboard_buffer: KspPacket) -> List[KspPacket]:
    """All packets needed by keyboard to change key colors

    Args:
        color_keyboard_buffer (KspPacket): Modified (COLOR_KEYBOARD_BUFFER)

    Returns:
        List[KspPacket]: Packets to be sent to (KspKeyboard)
    """
    return [COLOR_KEYBOARD_START()] + color_keyboard_buffer.split_into_buffers(HYPERX_PACKET_BUFFER_SIZE)


def BRIGHTNESS_PACKETS(new_level: int) -> List[KspPacket]:
    """All packets needed by keyboard to set brightness of keys

    Args:
        new_level (int): New brightness level (0-255)

    Returns:
        List[KspPacket]: Packets to be sent to (KspKeyboard)
    """
    p_start = KspPacket(HYPERX_PACKET_BUFFER_SIZE)
    p_start.replace_at_offset([0x04, 0x57], 0)
    p_start.set_offset(0x01, 8)

    p_brightness = KspPacket(HYPERX_PACKET_BUFFER_SIZE)
    p_brightness.set_offset(new_level, 12)

    p_end = KspPacket(HYPERX_PACKET_BUFFER_SIZE)
    p_end.replace_at_offset([0x04, 0x02], 0)

    return [p_start, p_brightness, p_end]


KEYS = {
    'ESC': 0,
    'TILDE': 4,
    'TAB': 8,
    'CAPS': 12,
    'SHIFT': 16,
    'CTRL': 20,
    # ?: 24
    '1': 28,
    'Q': 32,
    'A': 36,
    'Z': 40,
    'L_WIN': 44,
    'F1': 48,
    '2': 52,
    'W': 56,
    'S': 60,
    'X': 64,
    'L_ALT': 68,
    'F2': 72,
    '3': 76,
    'E': 80,
    'D': 84,
    'C': 88,
    # ?: 92
    'F3': 96,
    '4': 100,
    'R': 104,
    'F': 108,
    'V': 112,
    # ?: 116,
    'F4': 120,
    '5': 124,
    'T': 128,
    'G': 132,
    'B': 136,
    'SPACE': 140,
    'F5': 144,
    '6': 148,
    'Y': 152,
    'H': 156,
    'N': 160,
    # ?:164
    'F6': 168,
    '7': 172,
    'U': 176,
    'J': 180,
    'M': 184,
    # ?:188
    'F7': 192,
    '8': 196,
    'I': 200,
    'K': 204,
    'COMMA': 208,
    'R_ALT': 212,
    'F8': 216,
    '9': 220,
    'O': 224,
    'L': 228,
    'POINT': 232,
    # ?:236
    'F9': 240,
    '0': 244,
    'P': 248,
    'SEMICOLON': 252,
    'SLASH': 256,
    'FN': 260,
    'F10': 264,
    'MIN': 268,
    'L_BRACKET': 272,
    'SLASH': 276,
    # ?:280
    # ?:284
    'F11': 288,
    'IS': 292,
    'R_BRACKET': 296,
    # ?:300
    # ?:304
    'OPTIONS': 308,
    'F12': 312,
    'BACKSPACE': 316,
    'BACKSLASH': 320,
    'L_ENTER': 324,
    'R_SHIFT': 328,
    'R_CTRL': 332,

    'PRINT_SCREEN': 336,
    'INS': 340,
    'DEL': 344,
    # ?:348
    # ?:352
    'L_ARROW': 356,
    'SCROLL_LOCK': 360,
    'HOME': 364,
    'END': 368,
    # ?:372
    'U_ARROW': 376,
    'D_ARROW': 380,
    'PAUSE_BREAK': 384,
    'PGUP': 388,
    'PGDN': 392,
    # ?:396
    # ?:400
    'R_ARROW': 404,

    # ?:408
    'NUMLK': 412,
    'N_7': 416,
    'N_4': 420,
    'N_1': 424,
    'N_0': 428,
    # ?:432
    'N_SLASH': 436,
    'N_8': 440,
    'N_5': 444,
    'N_2': 448,
    # ?:452
    # ?:456
    'N_STAR': 460,
    'N_9': 464,
    'N_6': 468,
    'N_3': 472,
    'N_DOT': 476,
    # ?:480
    'N_MIN': 484,
    'N_PLUS': 488,
    'N_ENTER': 500,
}
