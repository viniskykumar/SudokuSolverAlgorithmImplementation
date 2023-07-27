# Sudoku Solver Algorithm Implementation(in Python)


## Overview

This repository contains a simple implementation of a Sudoku solver algorithm in Python. Sudoku is a popular number puzzle game that involves filling a 9x9 grid with digits so that each column, each row, and each of the nine 3x3 subgrids (also known as "boxes") contains all of the digits from 1 to 9 without repetition.

The solver uses a backtracking algorithm to efficiently find the solution to the given Sudoku puzzle.

## How the Algorithm Works

The backtracking algorithm is a depth-first search algorithm that explores all possible combinations of numbers to find a valid solution. It works as follows:

1. **Find an empty cell**: Start from the top-left corner of the grid and search for the first cell that is not filled. If no empty cell is found, the puzzle is solved.

2. **Try a number**: Once an empty cell is found, try placing a number (1 to 9) in that cell.

3. **Check if the number is valid**: Verify if the number placed in the cell is valid according to Sudoku rules. The number should not already exist in the same row, column, or the 3x3 subgrid it belongs to.

4. **Recursion**: If the number placed is valid, move on to the next empty cell and repeat steps 2 and 3. If the number is not valid, try the next number. If all numbers have been tried and none of them lead to a valid solution, backtrack to the previous cell and try a different number there.

5. **Base case**: The algorithm continues recursively until either a solution is found (all cells are filled without violating Sudoku rules) or no solution exists.


## How to Use

1. Clone the repository to your local machine.

2. Make sure you have Python installed (Python 3.x is recommended).

3. Open a terminal or command prompt and navigate to the repository's directory.

4. Run the `main.py` script using Python:

   ```bash
   python main.py

