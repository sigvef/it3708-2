from ea.solve import solve
from ea.adult_selection import full_generational_replacement
from ea.parent_selection import fitness_proportionate_selection
from ea.crossover import genome_component_crossover
from ea.mutation import per_genome_component_mutation
from ea.genotypes import BitVectorGenotype


class OneMax(object):

    problem_size = 40
    children_pool_size = 200
    adult_pool_size = 200
    fitness_satisfaction_threshold = problem_size
    maximum_generations = 20000
    select_adults = full_generational_replacement()
    select_parent = fitness_proportionate_selection()
    crossover = genome_component_crossover()
    mutate = per_genome_component_mutation(probability=0.001)

    def phenotype(self, genotype):
        return genotype

    def calculate_fitness(self, genotype):
        return sum(self.phenotype(genotype))

    def initial_population(self):
        return [BitVectorGenotype(self.problem_size)
                for j in range(self.children_pool_size)]


def main():
    print solve(OneMax())

main()
