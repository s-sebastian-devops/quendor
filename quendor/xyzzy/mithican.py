class Memory:
    def __init__(self, memory):
        self.memory = bytearray(memory)


def execute(story_data):
    print("\nA hollow voice says 'As you wish...'\n")

    Memory(story_data)
