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

## Performance
- Average Time (5 runs): 8.59 ± 3.92 seconds
- Best Time: ~2 seconds
- Worst Case: < 30 seconds

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
 
## Customization
- The expermient performance can be tweaked through several parameters:
  - Board Size: Set board_size to any integer n >= 4.
  - Population Size: Controls the number of individuals per generation.
  - Selection Subset Size: Determines tournament selection pressure (default is 4).
  - Mutation Rate: Increase to explore more variants early in search.
  - Crossover Rate: Controls how aggressively solutions recombine.
  - Cooling Factor (d): Used in the simulated annealing-inspired schedule.
 
## Licence
This project is licensed under the MIT License.

