# Genetic_Algorithm_Built_From_Scratch
A Python implementation of a genetic algorithm designed to efficiently solve the N-Queens problem. Originally developed to solve the classic 8-Queens puzzle, the algorithm has been extended to support arbitrary board sizes and optimized for performance through biologically inspired heuristics.

## Features
- Solves the 8-Queens problem in under 30 seconds (average ~8.59 seconds for base version).
- Extended version supports arbitrary board sizes (N-Queens).
- Implements biologically inspired techniques: mutation, crossover, selection.
- Incorporates simulated annealing-inspired cooling to improve convergence.
- Optimized selection and crossover strategies for faster solutions.
- Configurable mutation/crossover rates and population parameters.
- Visualization and logging support for analysis and debugging (optional).

## How It Works
- Initialization:
  - Starts with a randomly generated or semi-optimized population of chess boards.
  - Semi-optimized initialization ensures no adjacent queens, increasing initial fitness.
- Fitness Evaluation:
  - Fitness = 28 - number_of_attacks (for 8-Queens).
  - Higher fitness means fewer queen conflicts.
- Selection:
  - Tournament selection: pick the fittest individual from random subsets of the population.
- Crossover:
  - Two parents are combined at a random crossover point to create children.
- Mutation:
  - Each child may randomly reposition one queen to increase diversity.
- Cooling Schedule (Extended Version):
  - Simulated annealing approach where mutation and crossover rates are scaled down during learning.
