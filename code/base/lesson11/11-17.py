import pygame
import random
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
for i in range(100):
    width = random.randint(0, 250)
    height = random.randint(0, 100)
    top = random.randint(0, 400)
    left = random.randint(0, 500)
    line_width = random.randint(1,5)
    pygame.draw.rect(screen, [0, 0, 0], [left, top, width, height], line_width)
    pygame.display.flip()
    pygame.time.delay(30)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()