from typing import List
import hid
from time import sleep

class KspKeyboard():
    def __init__(self, hid_path: bytes) -> None:
        self.path = hid_path
        self.hid = None
    
    def connect(self):
        self.hid = hid.device()
        self.hid.open_path(self.path)
        self.hid.set_nonblocking(1)
    
    def send_feature_report(self, buffer: List, get_after: bool):
        written = self.hid.send_feature_report(buffer)
        read = -1
        if get_after:
            sleep(0.02)
            read = self.hid.get_feature_report(0, 0x64)
        return [written, read]
        