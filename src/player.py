import pygame
import logging


class Player:
    logger = logging.getLogger("Player")

    def __init__(self, player_images: list[pygame.Surface]):
        # TODO: add player's initial properties
        pass

    def __catch_keystrokes(self, deltatime):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            # TODO: add events for moving left
            pass

        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            # TODO: add events for moving right
            pass

        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            # TODO: add events for jumping
            pass

        else:
            # TODO: add events for standing still
            pass

    def __redraw(self, game_surface: pygame.Surface):
        # TODO: use game_surface.blit() based on the player directions
        pass

    def update(self, game_surface: pygame.Surface, deltatime: float):
        self.__catch_keystrokes(deltatime)
        self.__redraw(game_surface)
