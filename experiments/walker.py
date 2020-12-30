import logging

import pygame

from src.vector import Vector


class Walker:
    """A class that has the ability to be affected by forces"""
    logger = logging.getLogger('Player')

    def __init__(self, position: Vector, velocity: Vector):
        self.position = position
        self.velocity = velocity
        self.acceleration = Vector(0, 0)
        self.image = pygame.image.load('assets/images/icon.png')
        self.logger.info(f'init -> Walker -> pos={self.position}, vel={self.velocity}, acc={self.acceleration}')

    @classmethod
    def from_floats(cls, pos_x: float, pos_y: float, velocity_x: float, velocity_y: float):
        position = Vector(pos_x, pos_y)
        velocity = Vector(velocity_x, velocity_y)
        return cls(position, velocity)

    def update(self, mouse_x, mouse_y):
        self.acceleration.x = mouse_x - self.position.x
        self.acceleration.y = mouse_y - self.position.y
        self.acceleration.set_magnitude(0.01)

        self.velocity.add(self.acceleration)
        self.velocity.limit(1)

        self.position.add(self.velocity)

    def redraw(self, game_surface: pygame.Surface):
        game_surface.blit(self.image, (self.position.x, self.position.y))
