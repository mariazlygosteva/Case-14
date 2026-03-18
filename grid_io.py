'''
Module for Role A: grid generation and manipulation for Conway's Game of Life.
Provides functions to create empty or random grids, load/save from/to files,
and set individual cell states.
'''
import random


def create_empty_grid(rows: int, cols: int) -> list[list[int]]:
    '''Create an empty grid (all cells dead).'''
    return [[0 for _ in range(cols)] for _ in range(rows)]


def random_grid(rows: int, cols: int, prob: float = 0.5) -> list[list[int]]:
    '''Fill the grid with random values, each cell alive with given probability.'''
    return [[1 if random.random() < prob else 0 for _ in range(cols)]
            for _ in range(rows)]


def load_grid_from_file(filename: str) -> list[list[int]]:
    '''Read a grid from a text file. The file format is to be defined by the team.'''
    with open(filename) as f:
        return [list(map(int, l.split())) for l in f]


def save_grid_to_file(grid: list[list[int]], filename: str) -> None:
    '''Save the grid to a file.'''
    with open(filename, 'w') as f:
        for row in grid:
            f.write(' '.join(map(str, row)) + '\n')


def set_cell(grid: list[list[int]], row: int, col: int, value: int) -> None:
    '''Set the state of a specific cell (useful for mouse drawing).'''
    if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
        grid[row][col] = value
