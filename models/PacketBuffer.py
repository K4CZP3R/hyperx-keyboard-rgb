import os

class PacketBuffer(object):
    def __init__(self, size: int):
        self.content = [0]*size
    
    def get_offset(self, offset: int):
        return self.content[offset]
    def set_offset(self, value: int, offset: int):
        self.content[offset] = value
    def replace_at_offset(self, values: [int], offset: int):
        for i in range(0, len(values)):
            self.content[offset + i] = values[i]
    def get(self):
        if os.name == 'nt':
            return [len(self.content)] + self.content
        else:
            return self.content
    def get_raw(self):
        return self.content

    def split_into_buffers(self, size):
        splitted = []
        for i in range(0, len(self.content), size):
            _pb = PacketBuffer(size)
            _pb.replace_at_offset(self.content[i:i+size],0)
            splitted.append(_pb)
        return splitted