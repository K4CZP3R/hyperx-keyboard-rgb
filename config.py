from models.PacketBuffer import PacketBuffer as pb

HYPERX_PACKET_BUFFER_SIZE = 64


def GET_COLOR_PACKET_START():
    _p = pb(HYPERX_PACKET_BUFFER_SIZE)
    _p.replace_at_offset([0x04, 0xf2],0)
    return _p

def GET_COLOR_PACKET(r,g,b):
    return [0x81, r,g,b]


def GET_KEYBOARD_PACKET():
    _p = pb(HYPERX_PACKET_BUFFER_SIZE)
    for i in range(0, HYPERX_PACKET_BUFFER_SIZE, 4):
        _p.replace_at_offset(GET_COLOR_PACKET(0,0,0),i)
    return _p

def GET_WHOLE_COLOR_KEYBOARD_BUFFER():
    BUFFER_LEN = 64*9
    BUFFER = pb(BUFFER_LEN)
    for i in range(0, BUFFER_LEN, 64):
        BUFFER.replace_at_offset(GET_KEYBOARD_PACKET().get_raw(), i)
    return BUFFER

def GET_BRIGHTNESS_PACKETS(new_level):
    _p_start = pb(HYPERX_PACKET_BUFFER_SIZE)
    _p_start.replace_at_offset([0x04,0x57],0)
    _p_start.set_offset(0x01, 8)

    _p_brightness = pb(HYPERX_PACKET_BUFFER_SIZE)
    _p_brightness.set_offset(new_level, 12)

    _p_end = pb(HYPERX_PACKET_BUFFER_SIZE)
    _p_end.replace_at_offset([0x04, 0x02],0)

    return [_p_start, _p_brightness, _p_end]





KEYS = {
    'ESC': 0,
    'TILDE': 4,
    'TAB': 8,
    'CAPS': 12,
    'SHIFT': 16,
    'CTRL': 20,
    #?: 24
    '1': 28,
    'Q': 32,
    'A': 36,
    'Z':40,
    'L_WIN': 44,
    'F1': 48,
    '2': 52,
    'W': 56,
    'S': 60,
    'X': 64,
    'L_ALT': 68,
    'F2':72,
    '3': 76,
    'E': 80,
    'D': 84,
    'C':88,
    #?: 92
    'F3':96,
    '4': 100,
    'R': 104,
    'F': 108,
    'V': 112,
    #?: 116,
    'F4': 120,
    '5': 124,
    'T': 128,
    'G': 132,
    'B': 136,
    'SPACE': 140,
    'F5': 144,
    '6': 148,
    'Y': 152,
    'H':156,
    'N':160,
    #?:164
    'F6': 168,
    '7': 172,
    'U': 176,
    'J': 180,
    'M': 184,
    #?:188
    'F7':192,
    '8': 196,
    'I': 200,
    'K': 204,
    'COMMA': 208,
    'R_ALT': 212,
    'F8': 216,
    '9': 220,
    'O':224,
    'L':228,
    'POINT':232,
    #?:236
    'F9':240,
    '0': 244,
    'P':248,
    'SEMICOLON':252,
    'SLASH':256,
    'FN':260,
    'F10':264,
    'MIN':268,
    'L_BRACKET':272,
    'SLASH':276,
    #?:280
    #?:284
    'F11': 288,
    'IS':292,
    'R_BRACKET':296,
    #?:300
    #?:304
    'OPTIONS':308,
    'F12':312,
    'BACKSPACE': 316,
    'BACKSLASH': 320,
    'L_ENTER': 324,
    'R_SHIFT':328,
    'R_CTRL': 332,

    'PRINT_SCREEN':336,
    'INS': 340,
    'DEL': 344,
    #?:348
    #?:352
    'L_ARROW':356,
    'SCROLL_LOCK':360,
    'HOME': 364,
    'END': 368,
    #?:372
    'U_ARROW': 376,
    'D_ARROW': 380,
    'PAUSE_BREAK': 384,
    'PGUP': 388,
    'PGDN': 392,
    #?:396
    #?:400
    'R_ARROW':404,

    #?:408
    'NUMLK': 412,
    'N_7': 416,
    'N_4': 420,
    'N_1': 424,
    'N_0': 428,
    #?:432
    'N_SLASH': 436,
    'N_8': 440,
    'N_5': 444,
    'N_2': 448,
    #?:452
    #?:456
    'N_STAR': 460,
    'N_9': 464,
    'N_6': 468,
    'N_3': 472,
    'N_DOT': 476,
    #?:480
    'N_MIN': 484,
    'N_PLUS': 488,
    'N_ENTER': 500,
}