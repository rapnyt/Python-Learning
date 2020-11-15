import pygame
import sys
import random


class Game(object):

    def __init__(self):
        # Config
        self.fps = 10
        self.resolution = (1280, 720)
        self.matrix_table = []
        for i in range(0, 1280, 20):
            for j in range(0, 720, 20):
                self.matrix_table.append((i, j))
        self.snake_parts_position = [185]
        self.snake_movement = 36
        self.new_apple_index = random.randint(185, 1074)
        while self.matrix_table[self.new_apple_index][0] < 100 or self.matrix_table[self.new_apple_index][1] < 100 or \
                self.matrix_table[self.new_apple_index][0] > 580 or self.matrix_table[self.new_apple_index][1] > 580:
            self.new_apple_index = random.randint(185, 1074)
        self.a = self.matrix_table[self.new_apple_index][0]
        self.b = self.matrix_table[self.new_apple_index][1]
        print(self.a, self.b)
        self.font_name = pygame.font.match_font('arial')

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
                self.movement()
                self.game_over()
                self.eating_apple()
                self.fps_delta -= 1 / self.fps

            # drawing
            print(self.matrix_table[self.snake_parts_position[0]][0], self.matrix_table[self.snake_parts_position[0]][1])

            self.display.fill((0, 0, 0))
            self.draw()
            pygame.display.flip()

    def tick(self):
        #input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_KP_2]:
            self.snake_movement = 1
        if keys[pygame.K_KP_4]:
            self.snake_movement = -36
        if keys[pygame.K_KP_6]:
            self.snake_movement = 36
        if keys[pygame.K_KP_8]:
            self.snake_movement = -1

    def movement(self):
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

    def draw(self):
        try:
            for i in self.snake_parts_position:
                pygame.draw.rect(self.display, (245, 125, 20), pygame.Rect(self.matrix_table[i][0], self.matrix_table[i][1], 20, 20))
            pygame.draw.rect(self.display, (0, 255, 0), pygame.Rect(self.a, self.b, 20, 20))
        except:
            pass

        # dots and brackets
        pygame.draw.rect(self.display, (255, 255, 255), pygame.Rect(110, 110, 1, 1))
        pygame.draw.lines(self.display, (255, 255, 255), True, [(100, 100), (600, 100), (600, 600), (100, 600)])
        for i in range(110, 600, 20):
            for j in range(110, 600, 20):
                pygame.draw.rect(self.display, (255, 255, 255), pygame.Rect(i, j, 1, 1))

    def new_apple(self):
        self.new_apple_index = random.randint(185, 1074)
        while self.matrix_table[self.new_apple_index][0] < 100 or self.matrix_table[self.new_apple_index][1] < 100 or self.matrix_table[self.new_apple_index][0] > 580 or self.matrix_table[self.new_apple_index][1] > 580:
            self.new_apple_index = random.randint(185, 1074)
        self.a = self.matrix_table[self.new_apple_index][0]
        self.b = self.matrix_table[self.new_apple_index][1]
        print(self.a, self.b)

    def eating_apple(self):
        if self.snake_parts_position[0] == self.new_apple_index:
            self.snake_parts_position[0] += self.snake_movement
            self.snake_parts_position.append(self.new_apple_index)
            self.new_apple()

    def game_over(self):
        if self.matrix_table[self.snake_parts_position[0]][0] < 100 or self.matrix_table[self.snake_parts_position[0]][1] < 100 or self.matrix_table[self.snake_parts_position[0]][0] > 580 or self.matrix_table[self.snake_parts_position[0]][1] > 580 :
            self.show_go_screen()
        if len(self.snake_parts_position) != len(set(self.snake_parts_position)):
            self.show_go_screen()

    def draw_text(self, surf, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)

    def show_go_screen(self):
        self.draw_text(self.display, "GAME OVER!", 64, 350, 300)
        self.draw_text(self.display, "Press a key to Continue", 18, 350, 400)
        pygame.display.flip()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYUP:
                    self.__init__()
                    waiting = False


if __name__ == "__main__":
    Game()
