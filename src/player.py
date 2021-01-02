import logging
from enum import Flag, auto

import pygame

from src.walker import Walker
from src.helpers.vector import Vector


class State(Flag):
    FACING_RIGHT = auto()
    FACING_LEFT = auto()
    RUNNING = auto()
    JUMPING = auto()
    FALLING = auto()
    PUSHING = auto()


class Player(Walker):
    logger = logging.getLogger("Player")

    def __init__(self, images: dict[str, list[pygame.Surface]], position: Vector):
        Walker.__init__(self, images, position)
        self.state = State.FACING_RIGHT
        self.jump_force = Vector(0, -3.8)
        self.__moving_right_force = Vector()
        self.__moving_left_force = Vector()
        self.moving_magnitude = 0.1
        self.logger.info(f'init -> Player -> pos={self.position}, mass={self.mass}')

    @property
    def moving_magnitude(self):
        return self.__moving_magnitude

    @moving_magnitude.setter
    def moving_magnitude(self, value: float):
        self.__moving_magnitude = value
        self.__moving_right_force.x = value
        self.__moving_left_force.x = -value

    def __bound_to_ground(self):
        # TODO: replace with collision system
        if self.position.y >= 500:
            self.position.y = 500
            self.velocity.y = 0
            self.state &= ~State.JUMPING & ~State.FALLING

    def __catch_keystrokes(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.apply_force(self.__moving_left_force)
            self.state |= State.RUNNING | State.FACING_LEFT
            self.state &= ~State.FACING_RIGHT
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.apply_force(self.__moving_right_force)
            self.state |= State.RUNNING | State.FACING_RIGHT
            self.state &= ~State.FACING_LEFT
        else:
            self.state &= ~State.RUNNING
            self.velocity.x = 0

        if State.JUMPING not in self.state:
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                self.apply_force(self.jump_force)
                self.state |= State.JUMPING

    def _redraw(self, game_surface: pygame.Surface, deltatime: float, flip: bool = False):
        # TODO: check if there is a better way to implement images_key
        if State.RUNNING in self.state:
            self.images_key = 'running'
        # jumping state
        elif State.JUMPING in self.state:
            # animating jumping is very slow ie: changing images when jumping
            self.images_key = 'jumping'
        else:  # Idle state
            self.images_key = 'idle'
        super()._redraw(game_surface, deltatime, flip)

    def update(self, game_surface: pygame.Surface, deltatime: float):
        self.__catch_keystrokes()
        self.__bound_to_ground()
        super().update(game_surface, deltatime)
        self._redraw(game_surface, deltatime, State.FACING_LEFT in self.state)
