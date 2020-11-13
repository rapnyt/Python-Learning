import pygame
import sys
import random


class Game(object):

    def __init__(self):
        # Config
        self.fps = 5
        self.resolution = (1280, 720)
        self.matrix_table = []
        for i in range(100, 590, 20):
            for j in range(100, 590, 20):
                self.matrix_table.append((i, j))
        self.snake_parts_position = [0]
        self.snake_movement = 25
        self.new_apple()

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

            #eating apple
            if self.snake_parts_position[0] == self.new_apple_index:
                self.snake_parts_position.append(self.new_apple_index)
                self.new_apple()

            # drawing
            self.display.fill((0, 0, 0))
            self.draw()
            pygame.display.flip()
            print(self.snake_parts_position)

    def tick(self):
        # input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_KP_2]:
            # self.snake_parts_position[0] += 1
            self.snake_movement = 1
        if keys[pygame.K_KP_4]:
            # self.snake_parts_position[0] -= 25
            self.snake_movement = -25
        if keys[pygame.K_KP_6]:
            # self.snake_parts_position[0] += 25
            self.snake_movement = 25
        if keys[pygame.K_KP_8]:
            # self.snake_parts_position[0] -= 1
            self.snake_movement = -1

        try:
            if len(self.snake_parts_position) > 1:
                for i in range(len(self.snake_parts_position) - 1, -1, -1):
                    if i > 0:
                        self.snake_parts_position[i] = self.snake_parts_position[i - 1]
                    elif i == 0:
                        self.snake_parts_position[0] += self.snake_movement
            else:
                self.snake_parts_position[0] += self.snake_movement
        except:
            pass
            print(i,"index error")
        # if len(self.snake_parts_position) > 1:
        #     for i in self.snake_parts_position:
        #         if self.snake_parts_position.index(i) == 0:
        #             self.temp = i
        #             self.snake_parts_position[self.snake_parts_position.index(i)] += self.snake_movement
        #         else:
        #             self.temp2 = self.snake_parts_position[self.snake_parts_position.index(i)]
        #             self.snake_parts_position[self.snake_parts_position.index(i)] = self.temp
        #
        # else:
        #     self.snake_parts_position[0] += self.snake_movement

    def draw(self):
        for i in self.snake_parts_position:
            pygame.draw.rect(self.display, (245, 125, 20), pygame.Rect(self.matrix_table[i][0], self.matrix_table[i][1], 20, 20))
        pygame.draw.rect(self.display, (0, 255, 0), pygame.Rect(self.a, self.b, 20, 20))

        # dots and brackets
        pygame.draw.rect(self.display, (255, 255, 255), pygame.Rect(110, 110, 1, 1))
        pygame.draw.lines(self.display, (255, 255, 255), True, [(100, 100), (600, 100), (600, 600), (100, 600)])
        for i in range(110, 600, 20):
            for j in range(110, 600, 20):
                pygame.draw.rect(self.display, (255, 255, 255), pygame.Rect(i, j, 1, 1))

    def new_apple(self):
        self.new_apple_index = random.randint(1, len(self.matrix_table) - 1)
        self.a = self.matrix_table[self.new_apple_index][0]
        self.b = self.matrix_table[self.new_apple_index][1]




if __name__ == "__main__":
    Game()
