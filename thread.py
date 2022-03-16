from threading import Thread
from time import sleep
from models.ksp_keyboard import KspKeyboard
from helpers.hyperx_alloy_origins import COLOR_KEYBOARD_BUFFER, COLOR_KEY, KEYS, COLOR_KEYBOARD_PACKETS


class Threaded:
    def __init__(self, path:bytes) -> None:
        self.keyboard = KspKeyboard(path)
        self.keyboard.connect()
        
        self.running = False
        self.keyboard_buffer = COLOR_KEYBOARD_BUFFER()

    def start(self):
        self.running = True
        self.thread = Thread(target = self.run)
        self.thread.start()

    def run(self):

        while self.running:
            for packet in COLOR_KEYBOARD_PACKETS(self.keyboard_buffer):
                self.keyboard.send_feature_report(packet.get(), True)
            sleep(5)
    
    def stop(self):
        self.running = False
    def wait(self):
        self.thread.join()

t = Threaded(input("path:").encode('ascii'))

t.start()

try:
    while True:
        c = COLOR_KEY(int(input("r:")), int(input("g:")),int(input("b:")))
        for i in KEYS.keys():
            t.keyboard_buffer.replace_at_offset(c, KEYS[i])
except KeyboardInterrupt:
    t.stop()
    t.wait()

