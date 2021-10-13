"""
Example Snake project by Bennett Kaufmann
This project uses pygame and could be used as a template to make similar games
and as an example for how to implement different basic concepts to use in python.
"""

import random
import pygame

# Initialize and create display
pygame.init()
display = pygame.display.set_mode((640,440)) # 640x440 resolution (16x11 grid)
clock = pygame.time.Clock()

pygame.display.set_caption("Example Snake")

U, R, D, L = range(4) # Set up to 0, right to 1, down to 2, left to 3

# Set starting values
def start():
    global snakepos, snakedir, snakes, applepos, started, frames
    # Set starting positions for snake and apple
    snakepos = [5, 5]
    snakedir = R
    snakes = [[5, 5], [4, 5], [3, 5]]
    applepos = [10, 5]

    # Whether the user has started the game by inputting
    started = False
    frames = 2

start()

# Return position of new apple (not anywhere where snake is)
def new_apple():
    total = 16 * 11 - len(snakes) # Number of squares without a snake segment

    newpos = random.randint(0, total - 1)

    # Remove 1 for every square without a snake, place apple at 0
    for x in range(16):
        for y in range(11):
            if [x, y] not in snakes:
                newpos -= 1

            if not(newpos):
                return [x, y]

    return [x, y]

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # User exit
            pygame.quit()
            exit()

        # Get keyboard input and change direction if pressed
        if event.type == pygame.KEYDOWN and frames < 0:
            started = True

            if event.key in {pygame.K_UP, pygame.K_w}:
                if snakedir != D:
                    snakedir = U
                    break

            elif event.key in {pygame.K_RIGHT, pygame.K_d}:
                if snakedir != L:
                    snakedir = R
                    break

            elif event.key in {pygame.K_DOWN, pygame.K_s}:
                if snakedir != U:
                    snakedir = D
                    break

            elif event.key in {pygame.K_LEFT, pygame.K_a}:
                if snakedir != R:
                    snakedir = L
                    break

    frames -= 1

    if started:
        # Collect apple if front of snake is on it
        if snakepos == applepos:
            applepos = new_apple()
            snakes += [snakes[-1].copy()]

        # Move front of snake
        if snakedir == U:
            snakepos[1] -= 1

        elif snakedir == R:
            snakepos[0] += 1

        elif snakedir == D:
            snakepos[1] += 1

        elif snakedir == L:
            snakepos[0] -= 1

        # Move rest of snake body
        snakes = [snakepos.copy()] + snakes[:-1]

        # Restart if collided with side or snake
        if snakepos[0] < 0 or snakepos[0] >= 16 or snakepos[1] < 0 or snakepos[1] >= 11:
            start()

        if snakepos in snakes[1:]:
            start()

    display.fill((0x20, 0x20, 0x20)) # Fill with background color

    # Display apple
    pygame.draw.rect(display, (0xff, 0x0, 0x0), pygame.Rect(applepos[0] * 40, applepos[1] * 40, 40, 40))

    # Display each snake segment
    for snake in snakes:
        pygame.draw.rect(display, (0x0, 0xff, 0x0), pygame.Rect(snake[0] * 40, snake[1] * 40, 40, 40))

    # Update display and wait for frame
    pygame.display.update()
    clock.tick(8)
