import logging


class Memory:
    def __init__(self, memory):
        self.memory = bytearray(memory)
        self.pc = None

        self.read_starting_address()

        logging.debug(f"Start address: \t {self.pc} \t {hex(self.pc)}")

    def read_starting_address(self):
        """
        The word at $06 contains the byte address of the first instruction to
        execute.
        """

        self.pc = self.read_u16_address(0x06)
        assert isinstance(self.pc, int)

    def read_u16_address(self, address):
        """
        Address numbers can be stored as two adjacent bytes.
        """

        return (self.memory[address] << 8) + self.memory[address + 1]


def execute(story_data):
    print("\nA hollow voice says 'As you wish...'\n")

    Memory(story_data)
