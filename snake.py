import pygame, sys

pygame.init()
display = pygame.display.set_mode((1280,720))
box = pygame.Rect(10,10,20,20)

while True:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_2:
            box.y -= 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_4:
            box.x -= 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_6:
            box.x += 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_8:
            box.y += 1
    # input
    if pygame.key.get_pressed() [pygame.K_2]:
        box.y -= 1
    if pygame.key.get_pressed() [pygame.K_2]:
        box.y -= 1
        if pygame.key.get_pressed()[pygame.K_2]:
            box.y -= 1
            if pygame.key.get_pressed()[pygame.K_2]:
                box.y -= 1
    # drawing
    display.fill((255,255,255))
    pygame.draw.rect(display, (245,125,20), box)
    pygame.display.flip()