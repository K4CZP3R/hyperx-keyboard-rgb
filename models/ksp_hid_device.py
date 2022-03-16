from typing import List


class KspHidSubDevice:
    """Subdevice containing unique path and interface
    """
    def __init__(self, enumerate_dict: dict) -> None:
        self.path = enumerate_dict['path']
        self.usages = []
        self.iface = enumerate_dict['interface_number']
    
    def add_usage(self, enumerate_dict: dict):
        self.usages.append(f"{hex(enumerate_dict['usage_page'])}/{hex(enumerate_dict['usage'])}")

    def __str__(self) -> str:
        return f"Path='{self.path.decode('ascii')}' Usages={len(self.usages)} {f'Interface={self.iface}' if self.iface != -1 else '' } "

class KspHidDevice:
    """Hid device obtained from hidapi
    """
    def __init__(self, enumerate_dict: dict) -> None:
        self.vid = hex(enumerate_dict['vendor_id'])
        self.pid = hex(enumerate_dict['product_id'])
        self.sn = enumerate_dict['serial_number']
        self.rel = enumerate_dict['release_number']
        self.manu = enumerate_dict['manufacturer_string']
        self.prod = enumerate_dict['product_string']

        self.subdevices: List[KspHidSubDevice] = []

        self.add_subdevice(enumerate_dict)
    
    def add_subdevice(self, enumerate_dict: dict):
        if self.vid != hex(enumerate_dict['vendor_id']) or self.pid != hex(enumerate_dict['product_id']):
            raise ValueError("VidPid mismatch!")
        
        for subdevice in self.subdevices:
            if subdevice.path == enumerate_dict['path']:
                subdevice.add_usage(enumerate_dict)
                return

        
        self.subdevices.append(KspHidSubDevice(enumerate_dict))

    def __str__(self) -> str:
        return f"{self.prod if len(self.prod) > 0 else '?'} by {self.manu} ({self.vid}/{self.pid}) (subdevices {len(self.subdevices)})"