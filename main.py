import numpy as np
import random
import cProfile
from datetime import datetime
import genetic_algorithm
from eight_queens_puzzle import EightQueensState


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