"""
This file works on reading a CSV level map and convert it into tiles
"""
import csv
import logging

import pygame

from src.spritesheet import SpriteSheet


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_id: int, x: int, y: int, spritesheet: SpriteSheet):
        pygame.sprite.Sprite.__init__(self)
        self.image = spritesheet.get_sprite_by_id(tile_id)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def draw(self, level_surface: pygame.Surface):
        level_surface.blit(self.image, (self.rect.x, self.rect.y))


class TileMap:
    logger = logging.getLogger("TileMap")

    def __init__(self, filename: str, spritesheet: SpriteSheet, render_tile_size: tuple[int, int], player_tile_id: int):
        self.__player_start_pos = None
        self.spritesheet = spritesheet
        self.level_size = 0, 0

        self.tiles = self.__load_tiles(filename, render_tile_size, player_tile_id)
        self.level_surface = pygame.Surface(self.level_size)
        self.level_surface.set_colorkey((0, 0, 0))
        self.__load_level()

    def update(self, game_surface: pygame.Surface):
        game_surface.blit(self.level_surface, (0, 0))

    def __load_level(self):
        for tile in self.tiles:
            tile.draw(self.level_surface)

    def __read_level_csv(self, filename: str):
        level_map = []
        with open(filename, 'r') as data:
            data = csv.reader(data, delimiter=',')
            for row in data:
                level_map.append(list(row))
        return level_map

    def __load_tiles(self, filename: str, render_tile_size: tuple[int, int], player_tile_id: int):
        tiles = []
        level_map = self.__read_level_csv(filename)
        x, y = 0, 0
        for row in level_map:
            x = 0
            for tile in row:
                tile_id = int(tile)
                if tile_id == player_tile_id:
                    self.logger.info("Found player's starting position")
                    self.player_start_pos = x * render_tile_size[0], y * render_tile_size[1]
                elif tile_id >= 0:
                    new_tile = Tile(tile_id, x * render_tile_size[0],
                                    y * render_tile_size[1], self.spritesheet)
                    tiles.append(new_tile)
                x += 1
            y += 1
        self.level_size = x * render_tile_size[0], y * render_tile_size[1]
        return tiles

    @property
    def player_starting_position(self):
        return self.player_start_pos
