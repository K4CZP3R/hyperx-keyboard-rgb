class KspColor:
    def __init__(self, r: int, g: int, b: int) -> None:
        self.color = [r, g, b]

    def get_instruction(self):
        return [0x81] + self.color
