from tools import Mixin
import random


def per_genome_mutation(probability=0.01):
    def fn(genome):
        if random.random() < probability:
            component_to_mutate = random.randint(0, len(genome) - 1)
            genome.flip_bit(component_to_mutate)
        return genome
    return Mixin(fn)


def per_genome_component_mutation(probability=0.01):
    def fn(genome):
        for i, _ in enumerate(genome):
            if random.random() < probability:
                genome.flip_bit(i)
        return genome
    return Mixin(fn)
