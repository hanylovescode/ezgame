import logging

import pygame

from src.vector import Vector


class Walker:
    """A class that has the ability to be affected by forces"""
    logger = logging.getLogger('Player')

    def __init__(self, position: Vector, velocity: Vector = Vector(), mass: float = 1):
        self.position = position
        self.velocity = velocity
        self.acceleration = Vector()
        self.mass = mass
        self.velocity_limit = None
        self.image = pygame.image.load('assets/images/icon.png')
        self.logger.info(f'init -> Walker -> pos={self.position}, vel={self.velocity}, mass={self.mass}')

    @classmethod
    def from_floats(cls, pos_x: float, pos_y: float, mass: float = 1):
        """Alternative method to initialize an instance"""
        return cls(Vector(pos_x, pos_y), mass=mass)

    @property
    def mass(self) -> float:
        return self.__mass

    @mass.setter
    def mass(self, new_value: float):
        if new_value > 0:
            self.__mass = new_value
        else:
            self.__mass = 1
            self.logger.warning(f'Setting the mass to {new_value} is failed, '
                                'mass is set to 1. Mass has to be greater than zero')

    def apply_force(self, force: Vector):
        """Applying force to the object using the formula A = F / M"""
        self.acceleration.x += force.x / self.mass
        self.acceleration.y += force.y / self.mass

    def apply_forces_list(self, forces: list[Vector]):
        """Applies list of forces upon the object using the formula A = sum(F) / M"""
        # TODO: not sure which one has a better performance
        # self.acceleration.x += sum(f.x for f in forces) / self.mass
        # self.acceleration.y += sum(f.y for f in forces) / self.mass
        for f in forces:
            self.apply_force(f)

    def update(self):
        self.velocity.add(self.acceleration)
        if self.velocity_limit:
            self.velocity.limit(self.velocity_limit)

        self.position.add(self.velocity)
        self.acceleration.set(0, 0)

    def redraw(self, game_surface: pygame.Surface):
        game_surface.blit(self.image, (self.position.x, self.position.y))
