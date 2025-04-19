import numpy as np
import random
import cProfile
from datetime import datetime

"""Implements one random board constellation in the eight queen puzzle"""
class EightQueensState:
    def __init__(self, state=None):
        self.n = 8
        self.state = np.random.randint(0, self.n, self.n)
        self.fitness_value = self.fitness()

    # Calculates the fitness of a board state
    def fitness(self):
        
        # Counts the number of queen attacks
        count = 0
        
        # Iterates through all rows and counts the attacks
        for i in range(self.n - 1):
            
            # Saves the queens position as well as the position of subsequent queens 
            right_queen_pos = np.array(self.state[i + 1:])
            queen_pos = np.array(self.state[i])
            
            # for each queen, add one for every queen to the right
            count += (queen_pos == right_queen_pos).sum()
            
            # for each queen, add one for every queen on the same diagonal
            diagonal = np.arange(1, self.n - i)
            upper_diagonal = queen_pos + diagonal
            lower_diagonal = queen_pos - diagonal
            
            count += (right_queen_pos == upper_diagonal).sum()
            count += (right_queen_pos == lower_diagonal).sum()
        
        # Returns fitness score, highest possible score is 28
        return 28 - count
    
    
    # Implements mutation by changing one queen position to any other position on the row
    def mutate(self, mut_rate):
        if np.random.rand() < mut_rate:
            
            # Determines which queen to mutate
            pos = np.random.randint(self.n)
            
            # Determines how to move the queen on the row
            value = np.random.randint(self.n)
            
            self.state[pos] = value
            self.fitness_value = self.fitness()

    # Determines, if goal state was reached
    def is_goal(self):
        return self.fitness() == 28

    # Prints out the current board state
    def print_current_state(self):
        print("  ", end='')
        for i in range(len(self.state)):
            print(f"{i} ", end='')
        print()
        for i in reversed(range(len(self.state))):
            print(f"{i}", end=' ')
            for j in self.state:
                if i == j:
                    print("X", end=' ')
                else:
                    print("O", end=' ')
            print()
            
        if self.is_goal():
            print(f"Goal state was reached! fitness: {self.fitness_value}")
        else:
            print(f"Goal state was not reached yet! fitness: {self.fitness_value}")
        print()


"""Implements one random board constellation in the eight queen puzzle of any size n"""
class EightQueensStateModified:
    def __init__(self, n, state=None):
        self.n = n
        
        # The state is not completely randomly, but by propagating element (n-1) + 2
        predefined_state = []
        for n in range(self.n):
            # predefined_state.append(np.random.randint(self.n))
            if n == 0:
                predefined_state.append(np.random.randint(self.n))
            else:
                predefined_state.append((predefined_state[n-1]+2) % self.n)
        self.state = np.array(predefined_state)
        #self.state = np.random.randint(0, self.n, self.n)
        self.max_fitness = sum([i for i in range(self.n)])
        self.fitness_value = self.fitness()
    
    # Calculates the fitness of a board state
    def fitness(self):
        
        # Counts the number of queen attacks
        count = 0
        
        # Iterates through all rows and counts the attacks
        for i in range(self.n - 1):
            
            # Saves the queens position as well as the position of subsequent queens 
            right_queen_pos = np.array(self.state[i + 1:])
            queen_pos = np.array(self.state[i])
            
            # for each queen, add one for every queen to the right
            count += (queen_pos == right_queen_pos).sum()
            
            # for each queen, add one for every queen on the same diagonal
            diagonal = np.arange(1, self.n - i)
            upper_diagonal = queen_pos + diagonal
            lower_diagonal = queen_pos - diagonal
            
            count += (right_queen_pos == upper_diagonal).sum()
            count += (right_queen_pos == lower_diagonal).sum()
        
        # Returns fitness score, highest possible score is dependent on n
        return self.max_fitness - count
    
    
    # Implements mutation by changing one queen position to any other position on the row
    def mutate(self, mut_rate):
        if np.random.rand() < mut_rate:
           
            # Determines which queen to mutate
            pos = np.random.randint(self.n)
            
            # Determines how to move the queen on the row
            value = np.random.randint(self.n)
            
            self.state[pos] = value
            self.fitness_value = self.fitness()
            
            if self.fitness_value == self.max_fitness:
                return self.fitness_value, self

    # Determines, if goal state was reached
    def is_goal(self):
        return self.fitness() == self.max_fitness

    
    # Prints out the current board state
    def print_current_state(self):
        print("  ", end='')
        for i in range(len(self.state)):
            print(f"{i} ", end='')
        print()
        for i in reversed(range(len(self.state))):
            print(f"{i}", end=' ')
            for j in self.state:
                if i == j:
                    print("X", end=' ')
                else:
                    print("O", end=' ')
            print()
            
        if self.is_goal():
            print(f"Goal state was reached! fitness: {self.fitness_value}/{self.max_fitness}")
        else:
            print(f"Goal state was not reached yet! fitness: {self.fitness_value}/{self.max_fitness}")
        print()