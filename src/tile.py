import os
import csv
import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, image, x, y, spritesheet):
        pygame.sprite.Sprite.__init__(self)
        self.image = spritesheet.parse_sprite(image)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))


# TODO: fix TileMap class
class TileMap:
    def __init__(self, filename, spritesheet):
        self.tile_size = 16
        self.start_x, self.start_y = 0, 0
        self.spritesheet = spritesheet
        self.filename = filename
        self.level_width = 0
        self.level_height = 0

        self.tiles = self.__load_tiles()
        self.level_surface = pygame.Surface((self.level_width, self.level_height))
        self.level_surface.set_colorkey((0, 0, 0))
        self.__load_level()

    def update(self, surface):
        surface.blit(self.level_surface, (0, 0))

    def __load_level(self):
        for tile in self.tiles:
            tile.draw(self.level_surface)

    def __read_level_csv(self):
        level_map = []
        with open(os.path.join(self.filename), 'r') as data:
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
                if tile == '0':
                    self.start_x = x * self.tile_size
                    self.start_y = y * self.tile_size
                elif tile == '1':
                    tiles.append(Tile('grass.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '2':
                    tiles.append(Tile('grass2.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                x += 1
            y += 1
        self.level_width = x * self.tile_size
        self.level_height = y * self.tile_size
        return tiles
