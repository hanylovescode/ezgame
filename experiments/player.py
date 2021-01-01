import logging
from enum import Flag, auto

import pygame

from src.helpers.vector import Vector
from experiments.walker import Walker


class State(Flag):
    FACING_RIGHT = auto()
    FACING_LEFT = auto()
    MOVING = auto()
    JUMPING = auto()
    FALLING = auto()
    PUSHING = auto()


class Player(Walker):
    logger = logging.getLogger('Player')

    def __init__(self, images: pygame.Surface, position: Vector, mass: float = 1):
        Walker.__init__(self, images, position, mass=mass)

        self.state = State.FACING_RIGHT
        self.jump_force = Vector(0, -10)
        self.__moving_right_force = Vector()
        self.__moving_left_force = Vector()
        self.moving_magnitude = 0.1

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
        if self.position.y >= 540:
            self.position.y = 540
            self.velocity.y = 0
            self.state &= ~State.JUMPING

    def __catch_keystrokes(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.apply_force(self.__moving_left_force)
            self.state |= State.MOVING | State.FACING_LEFT
            self.state &= ~State.FACING_RIGHT
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.apply_force(self.__moving_right_force)
            self.state |= State.MOVING | State.FACING_RIGHT
            self.state &= ~State.FACING_LEFT
        else:
            self.state &= ~State.MOVING

        if State.JUMPING not in self.state:
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                self.apply_force(self.jump_force)
                self.state |= State.JUMPING

    def update(self, deltatime: float):
        self.__catch_keystrokes()
        self.__bound_to_ground()
        super().update(deltatime)
