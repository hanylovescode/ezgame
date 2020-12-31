import json
import logging

import pygame

from .settings import Settings
from .gameclock import GameClock
from .player import Player
from .spritesheet import SpriteSheet
from .tile import TileMap


class Level:
    logger = logging.getLogger("Level")

    def __init__(self, level_id: int, settings: Settings, game_clock: GameClock):
        self.settings = settings
        self.game_clock = game_clock

        level_loader = LevelLoader(level_id)
        self.level_map = level_loader.get_level_map()

        self.player = Player(level_loader.get_player_images(), self.level_map.player_start_pos)

        # TODO: initialize environment
        # self.walls =
        # self.door =
        # self.ladders =
        # ....

    def update(self):
        self.game_clock.update(self.settings.fps)

        game_surface = pygame.display.get_surface()
        game_surface.fill(self.settings.background_color)

        self.level_map.update(game_surface)
        self.player.update(game_surface, self.game_clock.deltatime)


class LevelLoader:
    logger = logging.getLogger("LevelLoader")

    def __init__(self, level_id: int):
        self.__level_id = level_id
        self.__assets_file = self.__load_assets_file()

        self.__player_spritesheet = self.__load_spritesheet('player_idle')
        self.__player_idle_images = self.__player_spritesheet.sprites

        self.__player_right_spritesheet = self.__load_spritesheet('player_walking_right')
        self.__player_walking_right_images = self.__player_right_spritesheet.sprites

        self.__player_images = {
            "idle": self.__player_idle_images,
            "walking_right": self.__player_walking_right_images,
        }

        self.__level_spritesheet = self.__load_spritesheet('tiles')
        self.__level_map = self.__load_level_map()
        self.__sounds = self.__load_sounds()

    def __load_assets_file(self):
        assets_file_path = f'assets/levels/L{self.__level_id}/assets.json'

        with open(assets_file_path, 'r') as f:
            data = f.read()

        self.logger.info('Assets file is loaded')
        return json.loads(data)

    def __load_spritesheet(self, object_name: str):
        # ss_obj stands for spritesheet json object
        ss_obj = self.__assets_file[object_name]
        # this determines the filepath
        ss_filepath = f'assets/{ss_obj["filepath"]}'

        ss_tile_size = ss_obj['tile_size']
        ss_render_tile_size = ss_obj['render_tile_size']

        return SpriteSheet(ss_filepath, ss_tile_size, ss_render_tile_size)

    def __load_level_map(self):
        level_map_path = f'assets/levels/L{self.__level_id}/map.csv'
        player_tile_id = self.__assets_file['tiles']['player_tile_id']
        render_tile_size = self.__assets_file['tiles']['render_tile_size']
        return TileMap(level_map_path, self.__level_spritesheet, render_tile_size, player_tile_id)

    def __load_sounds(self):
        # TODO: load sounds
        # self.logger.info("Sounds are loaded")
        return []

    def get_player_images(self):
        return self.__player_images

    def get_level_map(self):
        return self.__level_map
