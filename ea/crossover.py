from tools import Mixin
from genotypes import BitVectorGenotype
import random


def split_crossover():
    def fn(parent_a, parent_b):
        split = random.randint(0, len(parent_a) - 1)
        child = BitVectorGenotype(len(parent_a))
        for i, _ in enumerate(child):
            child[i] = parent_a[i] if i < split else parent_b[i]
        return child
    return Mixin(fn)


def genome_component_crossover():
    def fn(parent_a, parent_b):
        child = BitVectorGenotype(len(parent_a))
        for i, _ in enumerate(child):
            child[i] = parent_a[i] if random.random() < 0.5 else parent_b[i]
        return child
    return Mixin(fn)
