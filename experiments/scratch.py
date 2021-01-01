import logging

import pygame

from src.settings import Settings
from src.gameclock import GameClock
from src.gui import GUI
from src.helpers.vector import Vector
from experiments.player import Player


class Scratch(Settings):
    logger = logging.getLogger('Scratch')

    def __init__(self):
        Settings.__init__(self)

        pygame.init()
        pygame.display.set_mode((800, 600))

        self.game_clock = GameClock()
        self.game_gui = GUI()

        self.gravity = Vector(0, 1)
        self.wind = Vector(10, 0)
        image = pygame.image.load('assets/images/icon.png')
        self.player = Player(image, Vector(400, 300))

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

                if event.key == pygame.K_HOME:
                    self.fps = 60
                if event.key == pygame.K_END:
                    self.fps = 120
                if event.key == pygame.K_BACKQUOTE:
                    self.toggle_show_fps()
                if event.key == pygame.K_p:
                    self.toggle_game_pause()

    def __redraw(self):
        if self.is_game_paused:
            return

        game_surface = pygame.display.get_surface()
        game_surface.fill((0, 0, 0))

        self.player.apply_force(self.gravity)
        self.player.update(self.game_clock.fps)
        self.player.redraw(game_surface)

        self.game_gui.update(self.show_fps, self.game_clock.fps)

        pygame.display.flip()

    def __run(self):
        while self.game_is_running:
            self.game_clock.update(120)
            self.__catch_events()
            self.__redraw()
            self.logger.info(f'state: {self.player.state}')
        pygame.quit()


if __name__ == '__main__':
    logging.basicConfig(
        format='%(name)13s %(levelname)7s: %(message)s',
        level="INFO"
    )
    Scratch()
