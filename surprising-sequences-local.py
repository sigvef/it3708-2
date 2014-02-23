import random
from ea.solve import solve
from ea.adult_selection import full_generational_replacement
from ea.parent_selection import tournament_selection
from ea.crossover import genome_component_crossover
from ea.mutation import per_genome_component_mutation
from ea.genotypes import SymbolVectorGenotype

symbol_set_size = 20
problem_size = 402


class SurprisingSequences(object):

    def mutate_genome(genome, i):
        genome[i] = random.choice(range(1, symbol_set_size + 1))

    symbol_set_size = symbol_set_size
    problem_size = problem_size
    children_pool_size = 200
    adult_pool_size = 200
    fitness_satisfaction_threshold = 1
    maximum_generations = 100000
    select_adults = full_generational_replacement()
    select_parent = tournament_selection(k=8)
    crossover = genome_component_crossover()
    mutate = per_genome_component_mutation(probability=0.01,
                                           mutate=mutate_genome)

    def phenotype(self, genotype):
        phenotype = [genotype[i] for i in range(len(genotype))]
        return phenotype

    def calculate_fitness(self, genotype):

        phenotype = self.phenotype(genotype)

        found_sequences = set()
        collisions = 0
        for i in range(self.problem_size - 1):
                j = i + 1
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
        population = [SymbolVectorGenotype(self.symbol_set_size,
                                           self.problem_size)
                      for j in range(self.children_pool_size)]
        return population


def main():
    problem = SurprisingSequences()
    solution_genotype = solve(problem)
    print solution_genotype

main()
