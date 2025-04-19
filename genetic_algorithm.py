import numpy as np
import random
from eight_queens_puzzle import EightQueensState, EightQueensStateModified

class GeneticAlgorithm:
    """Solves the 8 Queens problem by implementing a genetic algorithm"""
    def __init__(self, population=None, pop_size=10,
                 mut_rate=0.75, recomb_rate=1,
                 max_runs=2400):
        
        self.mut_rate = mut_rate
        self.recomb_rate = recomb_rate
        self.pop_size = pop_size
        self.max_runs = max_runs
        
        # Creates a list of length pop_size containing Eight Queens Puzzles  
        if population==None:
            self.population=[EightQueensState() for _ in range(pop_size)]
    
    # Implements recombination by iterating through the population
    # two adjustent parents are chosen to create child constellation
    def recomb(self):
        for i in range(len(self.population)-1):
            if i % 2 == 0:
                if np.random.rand() < self.recomb_rate:
                    # Determins index of recombination
                    rec = np.random.randint(1, self.population[i].n)
                    
                    # Copies array to list, performs recombination
                    state1 = self.population[i].state.tolist()
                    state2 = self.population[i+1].state.tolist()
                    state1[:rec], state2[:rec] = state2[:rec], state1[:rec]
                    
                    # Safes child arrays inplace
                    self.population[i].state = np.array(state1)
                    self.population[i+1].state = np.array(state2)
                    self.population[i].fitness_value = self.population[i].fitness()
                    self.population[i+1].fitness_value = self.population[i+1].fitness()

    # Implements the mutation part of the genetic algorithm
    def mutate(self):
        for state in self.population:
            state.mutate(self.mut_rate)
            
    # Performs natural selection on the population to create new population
    def create_new_pop(self):
        new_pop = []
        
        
        for j in range(self.pop_size//5):
            # Chooses a random subpopulation of 4
            sub_population = random.choices(self.population, k=4)
        
            # Determines the fitness of the subpopulation
            for i in range(5):
                chosen_state = sub_population[0]
                max_fitness_value = chosen_state.fitness_value
                for state in sub_population[1:]:
                    if state.fitness_value > chosen_state.fitness_value:
                        chosen_state = state
                        max_fitness_value = state.fitness_value
                
                # Picks state with highest fitness
                new_pop.append(chosen_state)
                
        if max([state.fitness_value for state in new_pop]) < 20:
            self.population = [EightQueensState() for _ in range(self.pop_size)]
        else:
            self.population = new_pop          
                
    # Runs all aspects of the genetic algorithm
    def run(self):
        best_performance = 0
        run_counter = 0
        while best_performance != 28 and run_counter != self.max_runs:
            
            # Performs natural selection on the population
            self.create_new_pop()
            
            # Performs 1 cicles of recombination on the population
            self.recomb()
            
            # Performs 1 mutation cicle on the population
            self.mutate()
            
            # Finds best performing child state
            best_index = np.argmax([state.fitness_value for state in self.population])
            best_performance = self.population[best_index].fitness_value
            run_counter += 1
        
        return best_performance, self.population[best_index], run_counter