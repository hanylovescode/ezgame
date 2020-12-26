import pygame
import logging


class Player:
    logger = logging.getLogger("Player")

    def __init__(self, player_images: list[pygame.Surface]):
        self.player_images = player_images
        self.rect = player_images[0].get_rect()
        self.rect.y = 350
        self.jumping = False
        self.falling = False
        self.is_moving_right = False
        self.is_moving_left = False
        self.move = [0, 0]

    def __catch_keystrokes(self, deltatime: float):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.move[0] = -5 * deltatime
            self.is_moving_right = False
            self.is_moving_left = True
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.move[0] = 5 * deltatime
            self.is_moving_right = True
            self.is_moving_left = False
        else:
            self.is_moving_right = False
            self.is_moving_left = False
            self.move[0] = 0
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.__jump()

    def __redraw(self, game_surface: pygame.Surface):
        if self.is_moving_right:
            game_surface.blit(self.player_images[2], self.rect)
        elif self.is_moving_left:
            game_surface.blit(self.player_images[1], self.rect)
        else:
            game_surface.blit(self.player_images[0], self.rect)

    def __jump(self):
        if self.jumping is False:
            self.falling = False
            self.jumping = True

    def __move(self, deltatime: float):
        if self.jumping and not self.falling:
            self.move[1] = -5 * deltatime
        if self.rect.y < 0:
            self.falling = True
            self.move[1] = 5 * deltatime
        if self.falling and self.rect.y >= 350:
            self.falling = False
            self.jumping = False
            self.move[1] = 0
        self.rect.move_ip(self.move[0], self.move[1])

    def update(self, game_surface: pygame.Surface, deltatime: float):
        self.__catch_keystrokes(deltatime)
        self.__move(deltatime)
        self.__redraw(game_surface)
