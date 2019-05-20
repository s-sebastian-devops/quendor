import logging

from enum import Enum

OpForm = Enum("Form", "SHORT LONG VARIABLE EXTENDED")
OpCount = Enum("OpCount", "OP0 OP1 OP2 VAR")


class Memory:
    def __init__(self, memory):
        self.memory = bytearray(memory)
        self.pc = None

        self.version = self.memory[0x00]

        self.read_starting_address()

        logging.debug(f"Story file version: \t {self.version}")
        logging.debug(f"Start address: \t {self.pc} \t {hex(self.pc)}")

    def read_instruction(self, address):
        current_byte = address
        logging.debug(f"Current byte: \t {current_byte} \t ({hex(current_byte)})")

        opcode_byte = self.memory[address]
        logging.debug(f"Opcode byte: \t {opcode_byte} \t ({hex(opcode_byte)})")

        ########################################################
        # Determine the instruction form.
        ########################################################

        if self.version >= 5 and (opcode_byte == 0xBE):
            opcode = self.read_extended_opcode(self.memory[current_byte])
            opcode_form = OpForm.EXTENDED
            current_byte += 1
        elif opcode_byte & self.bin_of(96) == self.dec_of(0b01100000):
            opcode_form = OpForm.VARIABLE
        elif opcode_byte & self.bin_of(64) == self.dec_of(0b01000000):
            opcode_form = OpForm.SHORT
        else:
            opcode_form = OpForm.LONG

        logging.debug(f"Opcode form: \t {opcode_form.name}")

        ########################################################
        # Determine the operand count and type(s).
        ########################################################

        operand_count = self.read_operand_count(opcode_form, opcode_byte)
        logging.debug(f"Operand count: \t {operand_count.name}")

    def read_operand_count(self, opcode_form, opcode_byte):
        if opcode_form == OpForm.LONG:
            count = OpCount.OP2
        elif opcode_form == OpForm.SHORT:
            if opcode_byte & self.bin_of(48) == self.dec_of(0b00110000):
                count = OpCount.OP0
            else:
                count = OpCount.OP1
        elif opcode_form == OpForm.VARIABLE:
            if opcode_byte & self.bin_of(32) == self.dec_of(0b00100000):
                count = OpCount.VAR
            else:
                count = OpCount.OP2

        return count

    @staticmethod
    def read_extended_opcode(byte):
        print("extended opcode")
        pass

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
