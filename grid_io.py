'''
Module for Role A: grid generation and manipulation for Conway's Game of Life.
Provides functions to create empty or random grids, load/save from/to files,
and set individual cell states.
'''
import random


def create_empty_grid(rows: int, cols: int) -> list[list[int]]:
    '''
        The function creates a two-dimensional grid with all cells set to 0 (dead).

        Args:
            rows (int): Number of rows in the grid
            cols (int): Number of columns in the grid

        Returns:
            list[list[int]]: A list representing the grid with all cells dead
    '''
    return [[0 for _ in range(cols)] for _ in range(rows)]


def random_grid(rows: int, cols: int, prob: float = 0.5) -> list[list[int]]:
    '''
        The function creates a grid filled with random cell states based on
        a given probability of a cell being alive.

        Args:
            rows (int): Number of rows in the grid
            cols (int): Number of columns in the grid
            prob (float): Probability of a cell being alive (default is 0.5)

        Returns:
            list[list[int]]: A list representing the grid with random cell states
                            (1 for alive, 0 for dead)
    '''
    return [[1 if random.random() < prob else 0 for _ in range(cols)]
            for _ in range(rows)]


def load_grid_from_file(filename: str) -> list[list[int]]:
    '''
    The function reads a grid from a text file.
    File format: each line contains space-separated values (0 or 1)
    representing cell states in the grid.

    Args:
        filename (str): Path to the file containing the grid data

    Returns:
        list[list[int]]: A list representing the grid loaded from the file
    '''

    # File format:
    # 1 0 0 0 1
    # 0 1 0 1 1
    # 1 1 0 1 0
    # 1 0 1 0 1
    # 1 0 1 1 0

    with open(filename) as f:
        return [list(map(int, l.split())) for l in f]


def save_grid_to_file(grid: list[list[int]], filename: str) -> None:
    '''
    The function saves the grid to a text file.
    Each row of the grid is written as space-separated values (0 or 1).

    Args:
        grid (list[list[int]]): A list representing the grid to save
        filename (str): Path to the file where the grid will be saved
    '''

    # File format:
    # 1 0 0 0 1
    # 0 1 0 1 1
    # 1 1 0 1 0
    # 1 0 1 0 1
    # 1 0 1 1 0

    with open(filename, 'w') as f:
        for row in grid:
            f.write(' '.join(map(str, row)) + '\n')


def set_cell(grid: list[list[int]], row: int, col: int, value: int) -> None:
    '''
    The function sets the state of a specific cell in the grid.
    This is useful for mouse drawing and manual editing.

    Args:
        grid (list[list[int]]): A list representing the grid
        row (int): Row index of the cell to modify
        col (int): Column index of the cell to modify
        value (int): New value for the cell (1 for alive, 0 for dead)
    '''
    if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
        grid[row][col] = value
