import numpy as np
import random
import cProfile
from datetime import datetime
from genetic_algorithm import GeneticAlgorithm, GeneticAlgorithmModified
from eight_queens_puzzle import EightQueensState, EightQueensStateModified


if __name__ == "__main__":
    # Instantiates the Eight Queens Puzzle
    print("Here one Eight Queens Puzzle is instantiated, (X stands for the queens):")
    print()
    queen_puzzle = EightQueensState()
    queen_puzzle.print_current_state()

    print("Now one mutation round was performed on the state:")
    print()
    queen_puzzle.mutate(1)
    queen_puzzle.print_current_state()

    print("The genetic algorithm will find a solution state:")
    print()

    best_performance = 0
    t1 = datetime.now()
    while best_performance < 28:
            my_alg = GeneticAlgorithm(pop_size=5,
                                    max_runs=2400,
                                    mut_rate=0.2,
                                    recomb_rate=1)
            best_performance, state, run_counter = my_alg.run()
    delta = datetime.now() - t1
    state.print_current_state()
    print(f"Time needed to arrive at solution: {delta.total_seconds()} seconds")
            

    print("Average time needed to find a solution:")
    print()

    timed_results = []
    counter = 0
    while counter < 5:
        t1 = datetime.now()
        best_performance = 0
        while best_performance != 28:
            my_alg = GeneticAlgorithm(pop_size=5,
                                    max_runs=2400,
                                    mut_rate=0.2,
                                    recomb_rate=1)
            best_performance, state, run_counter = my_alg.run()
        delta = datetime.now() - t1
        timed_results.append(delta.total_seconds())
        counter += 1
        print(counter, delta)
        
        
    print("Average out of 5 trials: ", np.mean(timed_results))
    print("Standard deviation:", np.std(timed_results))

    solution_dictionary = {
    4 : 2,
    5 : 10,
    6 : 4,
    7 : 40,
    8 : 92,
    9 : 352,
    10 : 724
    }

    # Finds all solutions

    solutions_found = {}
    for board_size in [4, 5, 6, 7, 8, 9, 10]:
        t1 = datetime.now()
        solutions = []
        while len(solutions) != solution_dictionary[board_size]:
            while best_performance != sum([i for i in range(board_size)]):
                my_alg = GeneticAlgorithmModified(n=board_size,
                                                d=2,
                                                pop_size=5,
                                                max_runs=2400,
                                                mut_rate=1,
                                                recomb_rate=1)
                best_performance, best_state = my_alg.run()
            if best_state.state not in solutions:
                solutions.append(best_state.state)
        solutions_found[board_size] = solutions
        delta = datetime.now() - t1
        print(f"All solutions for n: {board_size} found! Time needed: {delta.total_seconds()}")


    # Finding solutions only with random rearrangement
    solutions_found = {}
    for board_size in [4, 5, 6]:
        t1 = datetime.now()
        solutions = []
        while len(solutions) != solution_dictionary[board_size]:
            random_puzzle = EightQueensStateModified(board_size)
            if random_puzzle.is_goal() and random_puzzle.state not in solutions:
                solutions.append(random_puzzle.state.state)
        solutions_found[board_size] = solutions
        delta = datetime.now() - t1
        print(f"All solutions for n: {board_size} found! Time needed: {delta.total_seconds()}")