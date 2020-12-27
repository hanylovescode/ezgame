"""
This file works on reading a CSV level map and convert it into tiles
"""
import csv
import pygame

from spritesheet import SpriteSheet


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_id: int, x: int, y: int, spritesheet: SpriteSheet):
        pygame.sprite.Sprite.__init__(self)
        self.image = spritesheet.get_sprite_by_id(tile_id)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def draw(self, game_surface: pygame.Surface):
        game_surface.blit(self.image, (self.rect.x, self.rect.y))


class TileMap:
    def __init__(self, filename: str, spritesheet: SpriteSheet):
        self.tile_size = 16
        # TODO: implement player start position
        self.player_start_x, self.player_start_y = 0, 0
        self.spritesheet = spritesheet
        self.filename = filename
        self.level_width = 0
        self.level_height = 0

        self.tiles = self.__load_tiles()
        self.level_surface = pygame.Surface((self.level_width, self.level_height))
        self.level_surface.set_colorkey((0, 0, 0))
        self.__load_level()

    def update(self, game_surface: pygame.Surface):
        game_surface.blit(self.level_surface, (0, 0))

    def __load_level(self):
        for tile in self.tiles:
            tile.draw(self.level_surface)

    def __read_level_csv(self):
        level_map = []
        with open(self.filename, 'r') as data:
            data = csv.reader(data, delimiter=',')
            for row in data:
                level_map.append(list(row))
        return level_map

    def __load_tiles(self):
        tiles = []
        level_map = self.__read_level_csv()
        x, y = 0, 0
        for row in level_map:
            x = 0
            for tile in row:
                if (tile_id := int(tile)) >= 0:
                    new_tile = Tile(tile_id, x * self.tile_size,
                                    y * self.tile_size, self.spritesheet)
                    tiles.append(new_tile)
                x += 1
            y += 1
        self.level_width = x * self.tile_size
        self.level_height = y * self.tile_size
        return tiles
