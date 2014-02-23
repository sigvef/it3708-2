from ea.solve import solve
from ea.adult_selection import full_generational_replacement
from ea.parent_selection import tournament_selection
from ea.crossover import genome_component_crossover
from ea.mutation import per_genome_component_mutation
from ea.genotypes import SymbolVectorGenotype
import random


class OneMax(object):

    def flip_bit(genome, i):
        genome[i] = 1 if genome[i] == 2 else 2

    problem_size = 40
    children_pool_size = 150
    adult_pool_size = 150
    fitness_satisfaction_threshold = 1
    maximum_generations = 1000
    select_adults = full_generational_replacement()
    select_parent = tournament_selection(k=8)
    crossover = genome_component_crossover(p=1)
    mutate = per_genome_component_mutation(probability=0.001, mutate=flip_bit)

    target = [1 if random.random() > 0.5 else 2 for i in range(problem_size)]

    def phenotype(self, genotype):
        return genotype

    def calculate_fitness(self, genotype):
        total = 0
        for i, component in enumerate(genotype):
            if component == self.target[i]:
                total += 2
            else:
                total += 1
        return total ** 2. /\
            ((self.problem_size * 2) ** 2)

    def initial_population(self):
        return [SymbolVectorGenotype(2, self.problem_size)
                for j in range(self.children_pool_size)]


def main():
    solved_generations = []
    for i in range(100):
        solved_in_generation = solve(OneMax())
        solved_generations.append(solved_in_generation)
        print i, solved_in_generation
    print solved_generations

main()
