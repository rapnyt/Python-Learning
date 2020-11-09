import pygame
import sys


class Game(object):

    def __init__(self):
        # Config
        self.fps = 1
        self.resolution = (1280, 720)
        self.box = pygame.Rect(100, 100, 20, 20)

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
            self.field_matrix_table()

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

    def draw(self):
        pygame.draw.rect(self.display, (245, 125, 20), self.box)
        pygame.draw.rect(self.display, (255, 255, 255), pygame.Rect(110, 110, 1, 1))
        pygame.draw.lines(self.display, (255, 255, 255), True, [(100, 100), (600, 100), (600, 600), (100, 600)])
        for i in range(110, 600, 20):
            for j in range(110, 600, 20):
                pygame.draw.rect(self.display, (255, 255, 255), pygame.Rect(i, j, 1, 1))

    def field_matrix_table(self):
        self.matrix_table = []
        for i in range(110, 600, 20):
            for j in range(110, 600, 20):
                self.matrix_table.append((i,j,False))
        pass

    def new_apple(self):
        pass

    def snake_movement(self):
        pass


if __name__ == "__main__":
    Game()
