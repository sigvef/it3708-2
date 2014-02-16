from ea.solve import solve
from ea.adult_selection import generational_mixing
from ea.parent_selection import tournament_selection
from ea.crossover import genome_component_crossover
from ea.mutation import per_genome_component_mutation
from ea.genotypes import BitVectorGenotype


class OneMax(object):

    problem_size = 40
    children_pool_size = 200
    adult_pool_size = 100
    fitness_satisfaction_threshold = problem_size
    maximum_generations = 20000
    select_adults = generational_mixing()
    select_parent = tournament_selection(k=8)
    crossover = genome_component_crossover()
    mutate = per_genome_component_mutation(probability=0.01)

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
