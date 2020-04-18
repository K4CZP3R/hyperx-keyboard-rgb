import hid
from time import sleep

class KspHid():
    def __init__(self, path: bytes):
        self.path = path
        self.hid = hid.device()

        self.hid.open_path(self.path)
        self.hid.set_nonblocking(1)

    def execute_packet_buffer(self, packet_buffer, get_after):
        self.hid.send_feature_report(packet_buffer)
        if get_after:
            sleep(0.02)
            return self.hid.get_feature_report(0,0x64)
        return None


class KspHidHelper():
    @staticmethod
    def get_interfaces_for_pidvid(vid, pid):
        _found_interfaces = [None]*16
        for d in hid.enumerate():
            if d['vendor_id'] == vid and d['product_id'] == pid:
                _found_interfaces[d['interface_number']] = d['path']
        
        last_index = 0
        for i in range(0, len(_found_interfaces)):
            if _found_interfaces[i] is not None:
                last_index += 1
            else:
                return _found_interfaces[:last_index]
        return _found_interfaces
    
    @staticmethod
    def get_interface_path_for_pidvid(vid, pid, interface_number):
        for d in hid.enumerate():
            if d['vendor_id'] == vid and d['product_id'] == pid and d['interface_number'] == interface_number:
                return d['path']
        return None