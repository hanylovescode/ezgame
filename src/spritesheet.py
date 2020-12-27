import pygame


class SpriteSheet:
    """
    This class takes an sprite sheet image and convert it to sprites
    Later on, we can retrieve the specific sprite by id
    """

    def __init__(self, filename: str, sprite_width: int, sprite_height: int):
        self.__filename = filename
        self.__sprite_width = sprite_width
        self.__sprite_height = sprite_height
        self.__sprite_sheet = pygame.image.load(filename).convert_alpha()
        self.__rect = self.__sprite_sheet.get_rect()
        self.__sprites = self.__get_all_sprites()

    def __get_sprite(self, x, y) -> pygame.Surface:
        sprite = pygame.Surface((self.__sprite_width, self.__sprite_height))
        sprite_rect = pygame.rect.Rect(x, y, self.__sprite_width, self.__sprite_height)
        sprite.blit(self.__sprite_sheet, (0, 0), sprite_rect)
        return sprite

    def __get_all_sprites(self):
        sprites = []
        columns = self.__rect.w // self.__sprite_width
        rows = self.__rect.h // self.__sprite_height

        counter = 0
        for r in range(rows):
            for c in range(columns):
                sprites.append(self.__get_sprite(c * self.__sprite_width, r * self.__sprite_height))
                counter += 1
        return sprites

    def get_sprite_by_id(self, sprite_id: int) -> pygame.Surface:
        return self.__sprites[sprite_id]
