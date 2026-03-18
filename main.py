'''
Main module (Role D) for Conway's Game of Life.
Coordinates the work of modules A, B, C, implements the main event loop,
controls simulation state and display.
'''

import pygame
import sys
import grid_io
import game_logic
import display
import ru_local as ru

ROWS = 30
COLS = 30
CELL_SIZE = 20
FPS = 30
INITIAL_SPEED = 200
SPEED_STEP = 50
MIN_SPEED = 0
MAX_SPEED = 1000

grid = []
generation = 0
running = False
speed = INITIAL_SPEED
last_update = 0


def main() -> None:
    '''
    Main program function.
    Initializes modules, runs the event loop, updates simulation state,
    and handles drawing.
    '''
    global grid, generation, running, speed, last_update

    screen, font, small_font = display.init_display(ROWS, COLS, CELL_SIZE)

    grid = grid_io.create_empty_grid(ROWS, COLS)
    generation = 0
    running = False
    speed = INITIAL_SPEED
    last_update = pygame.time.get_ticks()

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_q:
                        pygame.quit()
                        sys.exit()
                    case pygame.K_SPACE:
                        running = not running
                        last_update = pygame.time.get_ticks()
                    case pygame.K_s:
                        if not running:
                            grid = game_logic.next_generation(grid, wrap=True)
                            generation += 1
                    case pygame.K_r:
                        grid = grid_io.random_grid(ROWS, COLS, prob=0.5)
                        generation = 0
                        running = False
                    case pygame.K_c:
                        grid = grid_io.create_empty_grid(ROWS, COLS)
                        generation = 0
                        running = False
                    case pygame.K_l:
                        try:
                            grid = grid_io.load_grid_from_file('save.txt')
                            if len(grid) != ROWS or len(grid[0]) != COLS:
                                print(f'{ru.SIZE}')
                                grid = grid_io.create_empty_grid(ROWS, COLS)
                            generation = 0
                            running = False
                        except Exception as e:
                            print(f'{ru.LOADING}{e}')
                    case pygame.K_f:
                        try:
                            grid_io.save_grid_to_file(grid, 'save.txt')
                        except Exception as e:
                            print(f'{ru.SAVE}{e}')
                    case pygame.K_PLUS | pygame.K_KP_PLUS | pygame.K_EQUALS:
                        speed = max(MIN_SPEED, speed - SPEED_STEP)
                    case pygame.K_MINUS | pygame.K_KP_MINUS:
                        speed = min(MAX_SPEED, speed + SPEED_STEP)

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                cell = display.get_cell_from_mouse(pos, CELL_SIZE, ROWS, COLS)
                if cell is not None:
                    r, c = cell
                    if event.button == 1:
                        grid_io.set_cell(grid, r, c, 1)
                    elif event.button == 3:
                        grid_io.set_cell(grid, r, c, 0)

        now = pygame.time.get_ticks()
        if running and (now - last_update) >= speed:
            grid = game_logic.next_generation(grid, wrap=True)
            generation += 1
            last_update = now

        display.draw_grid(
            screen, grid, generation, speed,
            alive_color=display.DEFAULT_ALIVE_COLOR,
            dead_color=display.DEFAULT_DEAD_COLOR,
            grid_color=display.DEFAULT_GRID_COLOR,
            cell_size=CELL_SIZE,
            show_grid_lines=True
        )

        display.draw_ui(
            screen, font, small_font, generation, speed, running,
            text_color=display.DEFAULT_TEXT_COLOR
        )

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    main()