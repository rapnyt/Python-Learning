import pygame, sys

class Game(object):

    def __init__(self):
        # Config
        self.fps = 5

        # Init
        pygame.init()
        self.display = pygame.display.set_mode((1280,720))
        self.fps_clock = pygame.time.Clock()
        self.fps_delta = 0.0

        while True:


    def tick(self):
        pass

    def draw(self):
        pass


# box = pygame.Rect(10,10,20,20)

while True:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

    # ticking
    delta += clock.tick()/1000.0
    while delta > 1 / fps:
        delta -= 1 / fps

        # input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_KP_2]:
            box.y += 20
        if keys[pygame.K_KP4]:
            box.x -= 20
        if keys[pygame.K_KP6]:
            box.x += 20
        if keys[pygame.K_KP8]:
            box.y -= 20
        if box.x >= 1280:
            box.x = 0
        if box.y >= 720:
            box.y = 0
        if box.x < 0:
            box.x = 1280
        if box.y < 0:
            box.y = 720
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
        #     box.y -= 20
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_4:
        #     box.x -= 20
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_6:
        #     box.x += 20
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_8:
        #     box.y += 20
    # drawing
    display.fill((0,0,0))
    pygame.draw.rect(display, (245,125,20), box)
    # pygame.draw.circle(display, (255,0,0), circle, 20)
    pygame.display.flip()