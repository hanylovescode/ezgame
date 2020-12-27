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

        self.__player_images = self.__load_player_images()
        self.__level_spritesheet = self.__load_level_spritesheet()
        self.__level_map = self.__load_level_map()
        self.__sounds = self.__load_sounds()
        self.__fonts = self.__load_fonts()

    def __load_assets_file(self):
        assets_file_path = f'levels/L{self.__level_id}/assets.json'
        with open(assets_file_path, 'r') as f:
            data = f.read()
        self.logger.info('Assets file is loaded')
        return json.loads(data)

    def __load_fonts(self):
        fonts = {'fps': pygame.font.SysFont("Arial", 17)}
        self.logger.info("Fonts are loaded")
        return fonts

    def __load_player_images(self):
        player_images = []
        for i in self.__assets_file['player']:
            player_images.append(self.load_image(f'assets/{i}'))
        self.logger.info("Player images are loaded")
        return player_images

    def __load_level_spritesheet(self):
        # ss_obj stands for spritesheet json object
        ss_obj = self.__assets_file['tiles']
        ss_filepath = f'assets/{ss_obj["filepath"]}'
        ss_tile_size_x = int(ss_obj['tile_size_x'])
        ss_tile_size_y = int(ss_obj['tile_size_y'])
        return SpriteSheet(ss_filepath, ss_tile_size_x, ss_tile_size_y)

    def __load_level_map(self):
        level_map_path = f'levels/L{self.__level_id}/map.csv'
        return TileMap(level_map_path, self.__level_spritesheet)

    def __load_sounds(self):
        # TODO: load sounds
        # self.logger.info("Sounds are loaded")
        return []

    @staticmethod
    def load_image(image_path: str, with_alpha: bool = True):
        if with_alpha:
            return pygame.image.load(image_path).convert_alpha()
        return pygame.image.load(image_path).convert()

    def get_player_images(self):
        return self.__player_images

    def get_level_map(self):
        return self.__level_map

    def get_fonts(self):
        return self.__fonts
