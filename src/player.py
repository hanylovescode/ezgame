import pygame
import logging


class Player:
    logger = logging.getLogger("Player")

    def __init__(self, player_images: list[pygame.Surface], starting_pos: tuple[int, int]):

        self.player_images = player_images
        self.rect = player_images['idle'][0].get_rect()
        self.rect.x, self.rect.y = starting_pos

        self.player_idle_images = self.player_images['idle']
        self.player_walking_images = self.player_images['walking_right']
        self.image = pygame.Surface((0, 0))

        self.jumping = False
        self.falling = False

        self.is_moving_right = False
        self.is_moving_left = False
        self.move = [0, 0]

        self.index = 0
        self.animation_time = 0.1
        self.current_time = 0

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

    def __redraw(self, game_surface: pygame.Surface, deltatime: float):
        if self.is_moving_right:
            self.current_time += deltatime / 100
            if self.current_time >= self.animation_time:
                self.current_time = 0
                self.index = (self.index + 1) % len(self.player_walking_images)
                self.image = self.player_walking_images[self.index]
            game_surface.blit(self.image, self.rect)
        elif self.is_moving_left:
            self.current_time += deltatime / 100
            if self.current_time >= self.animation_time:
                self.current_time = 0
                self.index = (self.index + 1) % len(self.player_walking_images)
                self.image = self.player_walking_images[self.index]
            game_surface.blit(pygame.transform.flip(self.image, True, False), self.rect)
        else:
            self.current_time += deltatime / 100
            if self.current_time >= self.animation_time:
                self.current_time = 0
                self.index = (self.index + 1) % len(self.player_idle_images)
                self.image = self.player_idle_images[self.index]
            game_surface.blit(self.image, self.rect)

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
        self.__redraw(game_surface, deltatime)
