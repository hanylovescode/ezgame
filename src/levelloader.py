import pygame
import logging
import json

from spritesheet import SpriteSheet
from tile import TileMap


class LevelLoader:
    logger = logging.getLogger("LevelLoader")

    def __init__(self, level_id: int):
        self.__level_id = level_id
        self.__assets_file = self.__load_assets_file()

        self.__player_spritesheet = self.__load_spritesheet('player')
        self.__player_images = self.__player_spritesheet.sprites
        self.__level_spritesheet = self.__load_spritesheet('tiles')
        self.__level_map = self.__load_level_map()
        self.__sounds = self.__load_sounds()
        self.__fonts = self.__load_fonts()

    def __load_assets_file(self):
        assets_file_path = f'assets/levels/L{self.__level_id}/assets.json'
        with open(assets_file_path, 'r') as f:
            data = f.read()
        self.logger.info('Assets file is loaded')
        return json.loads(data)

    def __load_fonts(self):
        fonts = {'fps': pygame.font.SysFont("Arial", 17)}
        self.logger.info("Fonts are loaded")
        return fonts

    def __load_spritesheet(self, object_name: str):
        # ss_obj stands for spritesheet json object
        ss_obj = self.__assets_file[object_name]
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

    def get_fonts(self):
        return self.__fonts
