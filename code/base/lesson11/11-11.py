import pygame
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
my_ball = pygame.image.load('beach_ball.png')
screen.blit(my_ball, [50, 50])                   # draw the beach ball
pygame.display.flip()
pygame.time.delay(2000)
screen.blit(my_ball, [150, 50])                 # draw it again, somewhere else

# "erase" the first beach ballimage
pygame.draw.rect(screen, [255, 255, 255], [50, 50, 90, 90], 0)

pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
