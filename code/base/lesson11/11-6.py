import pygame
import random
from pygame.color import THECOLORS  # use color names

pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
for i in range(100):
    # pick random numbers for rectangle size and position
    width = random.randint(0, 250)
    height = random.randint(0, 100)
    top = random.randint(0, 400)
    left = random.randint(0, 500)

    # pick a random color by name
    color_name = random.choice(list(THECOLORS.keys()))
    color = THECOLORS[color_name]

    # pick a random line width, 1 to 3
    line_width = random.randint(1, 5)

    # draw the rectangle
    pygame.draw.rect(screen, color, [left, top, width, height], line_width)
    pygame.display.flip()
    pygame.time.delay(30)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
