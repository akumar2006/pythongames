import pygame
from sys import exit


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

# test_surface = pygame.image.load('graphics/Sky.png')
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()
#
#     screen.blit(test_surface,(200,100))
#
#     pygame.display.update()
#     clock.tick(60)



player = pygame.Rect((300, 250, 50, 50))

run = True
while run:

    screen.fill((0,0,0))

    pygame.draw.rect(screen, (255, 0, 0), player)

    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True or key[pygame.K_LEFT] == True:
        player.move_ip(-1,0)
    if key[pygame.K_d] == True or key[pygame.K_RIGHT] == True:
        player.move_ip(1,0)
    if key[pygame.K_w] == True or key[pygame.K_UP] == True:
        player.move_ip(0,-1)
    if key[pygame.K_s] == True or key[pygame.K_DOWN] == True:
        player.move_ip(0,1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()