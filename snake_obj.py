import pygame
import sys


class Game(object):

    def __init__(self):
        # Config
        self.fps = 5
        self.resolution = (1280, 720)
        self.box = pygame.Rect(10, 10, 20, 20)

        # Init
        pygame.init()
        self.display = pygame.display.set_mode(self.resolution)
        self.fps_clock = pygame.time.Clock()
        self.fps_delta = 0.0

        while True:
            # handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)

            # ticking
            self.fps_delta += self.fps_clock.tick() / 1000.0
            while self.fps_delta > 1 / self.fps:
                self.tick()
                self.fps_delta -= 1 / self.fps

            # drawing
            self.display.fill((0, 0, 0))
            self.draw()
            pygame.display.flip()

    def tick(self):
        # input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_KP_2]:
            self.box.y += 20
        if keys[pygame.K_KP4]:
            self.box.x -= 20
        if keys[pygame.K_KP6]:
            self.box.x += 20
        if keys[pygame.K_KP8]:
            self.box.y -= 20
        if self.box.x >= 1280:
            self.box.x = 0
        if self.box.y >= 720:
            self.box.y = 0
        if self.box.x < 0:
            self.box.x = 1280
        if self.box.y < 0:
            self.box.y = 720

    def draw(self):
        pygame.draw.rect(self.display, (245, 125, 20), self.box)


if __name__ == "__main__":
    Game()
