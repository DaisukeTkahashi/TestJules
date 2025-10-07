import pygame
import numpy as np

# Simulation settings
GRID_WIDTH = 200
GRID_HEIGHT = 150
CELL_SIZE = 4
WINDOW_WIDTH = GRID_WIDTH * CELL_SIZE
WINDOW_HEIGHT = GRID_HEIGHT * CELL_SIZE
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SAND_COLOR = (242, 224, 118)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Sand Simulation")
    clock = pygame.time.Clock()

    grid = np.zeros((GRID_WIDTH, GRID_HEIGHT), dtype=int)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Add sand with mouse
        if pygame.mouse.get_pressed()[0]:
            mx, my = pygame.mouse.get_pos()
            x, y = mx // CELL_SIZE, my // CELL_SIZE
            if 0 < x < GRID_WIDTH and 0 < y < GRID_HEIGHT:
                grid[x, y] = 1

        # Update grid
        for y in range(GRID_HEIGHT - 2, -1, -1):
            for x in range(GRID_WIDTH):
                if grid[x, y] == 1:
                    # Move down
                    if grid[x, y + 1] == 0:
                        grid[x, y] = 0
                        grid[x, y + 1] = 1
                    # Move diagonally
                    else:
                        left_free = x > 0 and grid[x - 1, y + 1] == 0
                        right_free = x < GRID_WIDTH - 1 and grid[x + 1, y + 1] == 0

                        if left_free and right_free:
                            if np.random.rand() < 0.5:
                                grid[x, y] = 0
                                grid[x - 1, y + 1] = 1
                            else:
                                grid[x, y] = 0
                                grid[x + 1, y + 1] = 1
                        elif left_free:
                            grid[x, y] = 0
                            grid[x - 1, y + 1] = 1
                        elif right_free:
                            grid[x, y] = 0
                            grid[x + 1, y + 1] = 1

        screen.fill(BLACK)

        # Draw grid
        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT):
                if grid[x, y] == 1:
                    pygame.draw.rect(screen, SAND_COLOR, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()
