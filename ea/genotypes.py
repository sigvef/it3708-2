import random


class BitVectorGenotype():

    def __init__(self, length):
        self.bits = [random.randint(0, 1) for i in range(length)]
        self.fitness = None

    def flip_bit(self, i):
        self.bits[i] ^= 1

    def __getitem__(self, i):
        return self.bits[i]

    def __setitem__(self, i, item):
        self.bits[i] = item

    def __len__(self):
        return len(self.bits)

    def __repr__(self):
        return ''.join(map(str, self.bits)) + ':' + str(self.fitness)

    def __int__(self):
        return reduce(lambda x, y: (x << 1) | y, self.bits)
