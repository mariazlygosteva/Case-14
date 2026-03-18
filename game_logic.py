'''
Module for Role B: game logic and boundary handling for Conway's Game of Life.
Provides functions to count live neighbors, apply boundary conditions,
and compute the next generation of the grid.
'''


def apply_boundary_condition(grid, row, col, wrap=False) -> tuple[int, int] | None:
    '''
    Apply boundary conditions to a cell coordinate.
    If wrap is True, use toroidal (wrap-around) boundaries.
    If wrap is False and the coordinate is inside the grid, return it unchanged.
    Otherwise return None.
    '''
    rows = len(grid)
    if rows > 0:
        cols = len(grid[0])
    else:
        cols = 0

    if rows == 0 or cols == 0:
        return None
    if wrap:
        return row % rows, col % cols
    if 0 <= row < rows and 0 <= col < cols:
        return row, col

    return None


def count_live_neighbors(grid, row, col, wrap=False) -> int:
    '''Count the number of live neighbors around the cell at (row, col).'''
    live_neighbors = 0

    for line in (-1, 0, 1):
        for column in (-1, 0, 1):
            if line == 0 and column == 0:
                continue

            neighbor = apply_boundary_condition(grid, row + line, col + column, wrap)
            if neighbor is None:
                continue

            neighbor_line, neighbor_column = neighbor
            live_neighbors += grid[neighbor_line][neighbor_column]

    return live_neighbors


def next_generation(grid, wrap=False) -> list[list[int]]:
    '''Compute the next generation of the grid according to Conway's rules.'''
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    if rows == 0 or cols == 0:
        return []

    new_grid = []
    for i in range(rows):
        row = [0] * cols
        new_grid.append(row)

    for row in range(rows):
        for col in range(cols):
            neighbors = count_live_neighbors(grid, row, col, wrap)
            current = grid[row][col]

            match (current, neighbors):
                case (1, 2 | 3):
                    new_grid[row][col] = 1
                case (0, 3):
                    new_grid[row][col] = 1
                case _:
                    new_grid[row][col] = 0

    return new_grid
