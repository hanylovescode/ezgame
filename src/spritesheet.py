import pygame


class SpriteSheet:
    """
    This class takes an sprite sheet image and convert it to sprites
    Later on, we can retrieve the specific sprite by id
    """

    def __init__(self, filename: str, sprite_size: tuple[int, int], render_size: tuple[int, int]):
        self.__filename = filename
        self.__sprite_size = sprite_size
        self.__sprite_sheet = pygame.image.load(filename).convert_alpha()
        self.__sprite_sheet.set_colorkey((0, 0, 0))
        self.__rect = self.__sprite_sheet.get_rect()
        self.__sprites = self.__get_all_sprites(render_size)

    def __get_sprite(self, location: tuple[int, int], render_size: tuple[int, int]) -> pygame.Surface:
        sprite = pygame.Surface(self.__sprite_size)
        sprite_rect = pygame.rect.Rect(*location, *self.__sprite_size)
        sprite.blit(self.__sprite_sheet, (0, 0), sprite_rect)
        sprite = pygame.transform.scale(sprite, render_size)
        sprite.set_colorkey((0, 0, 0))
        return sprite

    def __get_all_sprites(self, render_size):
        sprites = []
        columns = self.__rect.w // self.__sprite_size[0]
        rows = self.__rect.h // self.__sprite_size[1]

        for r in range(rows):
            for c in range(columns):
                location = c * self.__sprite_size[0], r * self.__sprite_size[1]
                sprites.append(self.__get_sprite(location, render_size))
        return sprites

    def get_sprite_by_id(self, sprite_id: int) -> pygame.Surface:
        return self.__sprites[sprite_id]

    @property
    def sprites(self):
        return self.__sprites
