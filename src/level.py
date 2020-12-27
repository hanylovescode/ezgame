import pygame
import logging

from settings import Settings
from levelloader import LevelLoader
from gameclock import GameClock
from gui import GUI
from player import Player


class Level:
    logger = logging.getLogger("Level")

    def __init__(self):
        self.settings = Settings()
        self.game_surface = pygame.display.set_mode(
            self.settings.screen_size,
            # pygame.HWSURFACE  # it solves flickering
        )

        self.levelloader = LevelLoader(1)
        self.level_map = self.levelloader.get_level_map()
        # TODO: read player position from TileMap
        # self.level_map.start_x
        # self.level_map.start_y

        pygame.display.set_caption(self.settings.game_title)
        # TODO: get an icon
        # icon = self.levelloader.images['icon']
        # pygame.display.set_icon(icon)

        # TODO: get a background image
        # self.background_image = self.levelloader.images['background']

        self.game_clock = GameClock()

        self.game_gui = GUI(self.levelloader.get_fonts())

        player_images = self.levelloader.get_player_images()
        self.player = Player(player_images)

        # TODO: initialize environment
        # self.walls =
        # self.door =
        # self.ladders =
        # ....

        self.game_is_running = True

    def __update(self):
        self.game_clock.update(self.settings.fps)

        if self.settings.is_game_paused:
            return

        # TODO: get a background image
        self.game_surface.fill((0, 0, 0))
        # self.game_surface.fill((34, 31, 49))

        self.level_map.update(self.game_surface)

        self.player.update(self.game_surface, self.game_clock.deltatime)

        self.game_gui.update(self.game_surface, self.settings.show_fps, self.game_clock.fps)

        pygame.display.flip()

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
                    self.settings.fps = 60
                if event.key == pygame.K_END:
                    self.settings.fps = 120
                if event.key == pygame.K_BACKQUOTE:
                    self.settings.toggle_show_fps()

                if event.key == pygame.K_p:
                    self.settings.toggle_game_pause()

    def run(self):
        self.logger.info('Game started running ...')
        while self.game_is_running:
            self.__catch_events()
            self.__update()
