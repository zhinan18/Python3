import pygame

pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
my_ball = pygame.image.load('beach_ball.png')
x = 50
y = 50
x_speed = 5  # how fast the ball will move:
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.time.delay(20)
    pygame.draw.rect(screen, [255, 255, 255],
                     [x, y, 90, 90], 0)
    x = x + x_speed  # move the ball
    if x > screen.get_width() - 90 or x < 0:  # check for hitting the sides
        x_speed = - x_speed  # reverse direction
    screen.blit(my_ball, [x, y])
    pygame.display.flip()

pygame.quit()
