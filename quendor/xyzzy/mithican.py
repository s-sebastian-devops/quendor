import logging


class Memory:
    def __init__(self, memory):
        self.memory = bytearray(memory)
        self.pc = None

        self.read_starting_address()

        logging.debug(f"Start address: \t {self.pc} \t {hex(self.pc)}")

    def read_instruction(self, address):
        current_byte = address
        logging.debug(f"Current byte: \t {current_byte} \t ({hex(current_byte)})")

        opcode_byte = self.memory[address]
        logging.debug(f"Opcode byte: \t {opcode_byte} \t ({hex(opcode_byte)})")

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

    @staticmethod
    def bin_of(number, length=8):
        value = format(number, "#0{}b".format(length + 2))
        assert set(value) <= set("b01")
        return int(value, 2)

    @staticmethod
    def dec_of(number):
        return int(number)


class CPU:
    @staticmethod
    def process(memory):
        instruction = memory.read_instruction(memory.pc)


def execute(story_data):
    print("\nA hollow voice says 'As you wish...'\n")

    memory = Memory(story_data)

    cpu = CPU()
    cpu.process(memory)
