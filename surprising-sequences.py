import math
from ea.solve import solve
from ea.adult_selection import generational_mixing
from ea.parent_selection import tournament_selection
from ea.crossover import genome_component_crossover
from ea.mutation import per_genome_component_mutation
from ea.genotypes import BitVectorGenotype


class SurprisingSequences(object):

    symbol_set_size = 10
    sequence_length = 26
    problem_size = int(math.ceil(
        math.log(symbol_set_size ** sequence_length, 2)))
    children_pool_size = 2000
    adult_pool_size = 2000
    fitness_satisfaction_threshold = 1
    maximum_generations = 2000
    select_adults = generational_mixing()
    select_parent = tournament_selection(k=8)
    crossover = genome_component_crossover()
    mutate = per_genome_component_mutation(probability=0.01)

    def phenotype(self, genotype):
        integer_representation = int(genotype)
        if integer_representation >\
                self.symbol_set_size ** self.sequence_length:
            return False

        phenotype = []
        while integer_representation:
            phenotype.append(integer_representation % self.symbol_set_size)
            integer_representation /= self.symbol_set_size
        while len(phenotype) < self.sequence_length:
            phenotype.append(0)

        return phenotype

    def calculate_fitness(self, genotype):

        phenotype = self.phenotype(genotype)

        if not phenotype:
            return 0

        found_sequences = set()
        collisions = 0
        for i in range(self.sequence_length):
            for j in range(i + 1, self.sequence_length):
                a = phenotype[i]
                b = phenotype[j]
                sequence = (a, b, j - i)
                if sequence in found_sequences:
                    collisions += 1
                else:
                    found_sequences.update([sequence])

        fitness = 1 / (1. + collisions)
        return fitness

    def initial_population(self):
        return [BitVectorGenotype(self.problem_size)
                for j in range(self.children_pool_size)]


def main():
    problem = SurprisingSequences()
    solution_genotype = solve(problem)
    print solution_genotype, problem.phenotype(solution_genotype)

main()
