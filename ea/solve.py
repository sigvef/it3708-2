

def solve(problem):

    children = problem.initial_population()
    adults = []
    generation = 0

    while (adults[-1].fitness if adults else 0) <\
            problem.fitness_satisfaction_threshold and\
            generation < problem.maximum_generations:
        print 'generation', generation
        if adults:
            print adults[-1]
            print problem.phenotype(adults[-1])

        for child in children:
            child.fitness = problem.calculate_fitness(child)
        adults = problem.select_adults(adults, children,
                                       problem.adult_pool_size)
        adults.sort(key=lambda x: x.fitness)
        parents = [(problem.select_parent(adults),
                    problem.select_parent(adults))
                   for i in range(problem.children_pool_size)]
        children = [problem.crossover(parent_a, parent_b)
                    for parent_a, parent_b in parents]
        children = [problem.mutate(child) for child in children]
        children.sort(key=lambda x: x.fitness)

        generation += 1

    return adults[-1]
