import pygame
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
pygame.draw.circle(screen, [255, 0, 0], [100, 100], 30, 0)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
