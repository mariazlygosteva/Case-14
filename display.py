'''
Display module (Role C) for Conway's Game of Life.
Responsible for initializing the Pygame window, drawing the grid and text information,
and converting mouse coordinates to cell indices.
'''

import pygame

DEFAULT_ALIVE_COLOR = (128, 0, 128)
DEFAULT_DEAD_COLOR = (0, 0, 0)
DEFAULT_GRID_COLOR = (64, 64, 64)
DEFAULT_TEXT_COLOR = (200, 150, 255)


def init_display(
        rows: int, cols: int, cell_size: int = 20,
        caption: str = "Conway's Game of Life"
) -> tuple[pygame.Surface, pygame.font.Font, pygame.font.Font]:
    '''
    Initialize the Pygame window, fonts and return drawing objects.

    Parameters:
        rows (int): number of grid rows.
        cols (int): number of grid columns.
        cell_size (int): cell size in pixels.
        caption (str): window title.

    Returns:
        Tuple (screen, font, small_font):
            screen (pygame.Surface): the display surface.
            font (pygame.font.Font): main font for text.
            small_font (pygame.font.Font): small font for additional info.
    '''
    pygame.init()
    pygame.font.init()

    width = cols * cell_size
    height = rows * cell_size
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(caption)

    font = pygame.font.Font(None, 24)
    small_font = pygame.font.Font(None, 18)

    return screen, font, small_font


def draw_grid(
        screen: pygame.Surface,
        grid: list[list[int]],
        generation: int,
        speed: float,
        alive_color: tuple[int, int, int] = DEFAULT_ALIVE_COLOR,
        dead_color: tuple[int, int, int] = DEFAULT_DEAD_COLOR,
        grid_color: tuple[int, int, int] = DEFAULT_GRID_COLOR,
        cell_size: int = 20,
        show_grid_lines: bool = True
) -> None:
    '''
    Draw the cell grid and grid lines.

    Parameters:
        screen: surface to draw on.
        grid: 2D list (rows x cols) with values 0 (dead) or 1 (alive).
        generation: current generation number (for display).
        speed: delay between generations in milliseconds (for display).
        alive_color: color of living cells.
        dead_color: color of dead cells.
        grid_color: color of grid lines.
        cell_size: cell size in pixels.
        show_grid_lines: whether to draw grid lines.
    '''
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    screen.fill(dead_color)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                rect = pygame.Rect(c * cell_size, r * cell_size, cell_size, cell_size)
                pygame.draw.rect(screen, alive_color, rect)

    if show_grid_lines:
        for x in range(0, cols * cell_size, cell_size):
            pygame.draw.line(screen, grid_color, (x, 0), (x, rows * cell_size))
        for y in range(0, rows * cell_size, cell_size):
            pygame.draw.line(screen, grid_color, (0, y), (cols * cell_size, y))


def draw_ui(
        screen: pygame.Surface,
        font: pygame.font.Font,
        small_font: pygame.font.Font,
        generation: int,
        speed: float,
        running: bool,
        text_color: tuple[int, int, int] = DEFAULT_TEXT_COLOR
) -> None:
    '''
    Draw text information over the grid: generation number,
    simulation speed, state (running/paused), and control hints.
    '''
    gen_text = f'Generation: {generation}'
    speed_text = f'Speed: {speed:.0f} ms'
    status_text = 'Running' if running else 'Paused'

    gen_surf = font.render(gen_text, True, text_color)
    speed_surf = small_font.render(speed_text, True, text_color)
    status_surf = small_font.render(status_text, True, text_color)

    margin = 5
    x_pos = margin
    y_pos_gen = margin
    y_pos_speed = y_pos_gen + gen_surf.get_height() + 2
    y_pos_status = y_pos_speed + speed_surf.get_height() + 4

    screen.blit(gen_surf, (x_pos, y_pos_gen))
    screen.blit(speed_surf, (x_pos, y_pos_speed))
    screen.blit(status_surf, (x_pos, y_pos_status))

    help_lines = [
        'Space: run/pause',
        'S: step',
        'R: random',
        'C: clear',
        'L: load',
        'F: save',
        '+/-: speed',
        'Q: quit',
        'LMB: alive',
        'RMB: dead'
    ]
    y = margin
    for line in help_lines:
        help_surf = small_font.render(line, True, text_color)
        x = screen.get_width() - help_surf.get_width() - margin
        screen.blit(help_surf, (x, y))
        y += help_surf.get_height() + 2


def get_cell_from_mouse(
        pos: tuple[int, int],
        cell_size: int,
        rows: int,
        cols: int
) -> tuple[int, int] | None:
    '''
    Convert mouse coordinates to grid cell indices.

    Parameters:
        pos: tuple (x, y) of mouse coordinates in the window.
        cell_size: cell size in pixels.
        rows: number of grid rows.
        cols: number of grid columns.

    Returns:
        Tuple (row, col) if the coordinates are inside the grid, otherwise None.
    '''
    x, y = pos
    col = x // cell_size
    row = y // cell_size
    if 0 <= row < rows and 0 <= col < cols:
        return row, col
    return None


def handle_color_scheme(
        alive_color: tuple[int, int, int] = DEFAULT_ALIVE_COLOR,
        dead_color: tuple[int, int, int] = DEFAULT_DEAD_COLOR,
        grid_color: tuple[int, int, int] = DEFAULT_GRID_COLOR
) -> dict:
    '''
    Return a dictionary with current colors (optional, for centralized management).

    Parameters:
        alive_color: color of living cells.
        dead_color: color of dead cells.
        grid_color: color of grid lines.

    Returns:
        Dictionary with keys 'alive', 'dead', 'grid'.
    '''
    return {
        'alive': alive_color,
        'dead': dead_color,
        'grid': grid_color
    }