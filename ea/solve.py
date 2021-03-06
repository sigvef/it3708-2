try:
    import numpypy as np
except:
    import numpy as np


def solve(problem):

    children = problem.initial_population()
    adults = []
    generation = 0

    print_stats_counter = 0
    print_stats_n = 5

    while (adults[-1].fitness if adults else 0) <\
            problem.fitness_satisfaction_threshold and\
            generation < problem.maximum_generations:
        #print 'generation', generation
        if adults:
            #print adults[-1]
            #print 'best:', adults[-1].fitness
            fitnesses = [x.fitness for x in adults]
            mean = np.mean(fitnesses)
            #std = np.std(fitnesses)
            if False and print_stats_counter % print_stats_n == 0:
                print '% generation', generation - 1
                print "\\addplot+["
                print "boxplot prepared={"
                print "median=%s," % np.median(fitnesses)
                print "upper quartile=%s," % np.percentile(fitnesses, 75)
                print "lower quartile=%s," % np.percentile(fitnesses, 25)
                print "upper whisker=%s," % max(fitnesses)
                print "lower whisker=%s" % min(fitnesses)
                print "},"
                print "] coordinates {};"
            print_stats_counter += 1

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

    fitnesses = [x.fitness for x in adults]
    mean = np.mean(fitnesses)
    std = np.std(fitnesses)
    if False:
        print '% generation', generation - 1
        print "\\addplot+["
        print "boxplot prepared={"
        print "median=%s," % np.median(fitnesses)
        print "upper quartile=%s," % (mean + std)
        print "lower quartile=%s," % (mean - std)
        print "upper whisker=%s," % max(fitnesses)
        print "lower whisker=%s" % min(fitnesses)
        print "},"
        print "] coordinates {};"
    return generation
    #return adults[-1]
