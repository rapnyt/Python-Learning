import pygame


class Launch(object):

    def __init__(self, game):
        self.game = game

    def tick(self):
        pass

    def draw(self):
        pygame.draw.rect(self.game.display, (245, 125, 20), self.game.box)



