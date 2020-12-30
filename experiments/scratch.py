import logging

import pygame

from src.gameclock import GameClock
from src.vector import Vector
from src.walker import Walker


class Scratch:
    logger = logging.getLogger('TestClass')

    def __init__(self):
        pygame.init()
        pygame.display.set_mode((800, 600))

        self.game_clock = GameClock()

        self.walker = Walker(Vector(400, 300), Vector(0, 0))

        self.game_is_running = True
        self.__run()

    def __catch_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.logger.warning('Game was forced to close!')
                self.game_is_running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game_is_running = False
                    self.logger.info('Game closed.')

    def __update(self):
        game_surface = pygame.display.get_surface()
        game_surface.fill((0, 0, 0))

        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.walker.update(mouse_x, mouse_y)

        self.walker.redraw(game_surface)

        pygame.display.flip()

    def __run(self):
        while self.game_is_running:
            self.__catch_events()
            self.game_clock.update(120)
            self.__update()
        pygame.quit()


if __name__ == '__main__':
    logging.basicConfig(
        format='%(name)13s %(levelname)7s: %(message)s',
        level="INFO"
    )
    Scratch()
