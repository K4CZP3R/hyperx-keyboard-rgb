
from os import stat
from platform import platform
from time import sleep
from typing import List, Optional
from hyperx_keyboard_rgb.exceptions.device_already_active import DeviceAlreadyActive
from hyperx_keyboard_rgb.models.ksp_hid_device import KspHidSubDevice
from hyperx_keyboard_rgb.exceptions.device_not_open import DeviceNotOpen
from hyperx_keyboard_rgb.helpers.hyperx_alloy_origins import COLOR_KEYBOARD_BUFFER, COLOR_KEYBOARD_PACKETS, COLOR_KEYBOARD_START
from hyperx_keyboard_rgb.models.ksp_color import KspColor
from hyperx_keyboard_rgb.helpers.ksp_hid_helper import KspHidHelper
import hid
from threading import Thread
from time import time
import os


class KeyboardHelper(object):
    @staticmethod
    def get_subdevice(vid: int, pid: int, interface: int) -> Optional[KspHidSubDevice]:
        vid = hex(vid)
        pid = hex(pid)
        devices = KspHidHelper.get_devices()

        for d in devices:
            if d.vid == vid and d.pid == pid:
                for sd in d.subdevices:
                    if sd.iface == interface:
                        return sd
        return None


class Keyboard(object):
    def __init__(self, device_path: bytes) -> None:
        self.device_path = device_path
        self.hid = None
        self.connected = False
        self.running = False
        self.thread = None

        self.__keyboard_buf = COLOR_KEYBOARD_BUFFER()
        self.__keyboard_start_buf = COLOR_KEYBOARD_START()

    @classmethod
    def from_ksp_hid_subdevice(cls, subdevice: KspHidSubDevice):
        return cls(device_path=subdevice.path)

    def connect(self):
        if self.running:
            raise DeviceAlreadyActive(
                "Thread for this device is running, stop it first!")
        self.hid = hid.device()
        self.hid.open_path(self.device_path)
        self.hid.set_nonblocking(1)
        self.connected = True

    def start_thread(self):
        if self.thread is not None:
            raise DeviceAlreadyActive(
                "Thread is already active, stop it first!")
        self.thread = Thread(target=self.__thread_loop)
        self.running = True
        self.thread.start()

    def stop_thread(self):
        if self.thread is None:
            raise DeviceNotOpen("There is no thread")
        self.running = False
        self.thread.join()
        self.thread = None

    def set_color(self, offset: int, color_key: KspColor):
        self.__keyboard_buf.replace_at_offset(
            color_key.get_instruction(), offset)

    def __thread_loop(self):
        while self.running:
            start = time()
            for packet in COLOR_KEYBOARD_PACKETS(self.__keyboard_buf):
                self.__send_feature_report(
                    packet.get(),  True if os.name == 'nt' else False)
            print(f"Took {time() - start}ms")

    def __send_feature_report(self, buffer: List[int], get_after: bool):
        if not self.connected:
            raise DeviceNotOpen(
                f"Device with path {self.device_path} is not open, call connect() first!")

        written = self.hid.send_feature_report(buffer)
        read = -1
        if get_after:
            sleep(.025)
            read = self.hid.get_feature_report(0, 0x64)
        return [written, read]
