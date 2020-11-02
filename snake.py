import pygame, sys

pygame.init()
display = pygame.display.set_mode((1280,720))

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

    pygame.draw.rect(display, (245,125,20), pygame.Rect(10,50,300,100))
    pygame.display.flip()