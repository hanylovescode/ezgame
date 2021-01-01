import logging

import pygame

from src.helpers.vector import Vector


class Walker:
    """A class that has the ability to be affected by forces"""
    logger = logging.getLogger('Player')

    def __init__(self, images: dict[str, list[pygame.Surface]],
                 position: Vector, velocity: Vector = Vector(),
                 mass: float = 1):
        self.position = position
        self.velocity = velocity
        self.acceleration = Vector()
        self.mass = mass
        self.velocity_limit = None

        self.images = images
        self.images_key = 'idle'
        self.image_index = 0
        self.current_image = self.images[self.images_key][self.image_index]

        self.animation_time = 0.1
        self.current_time = 0
        self.logger.info(f'init -> Walker -> pos={self.position}, vel={self.velocity}, mass={self.mass}')

    @classmethod
    def from_floats(cls, images: dict[str, list[pygame.Surface]], pos_x: float, pos_y: float, mass: float = 1):
        """Alternative method to initialize an instance"""
        return cls(images, Vector(pos_x, pos_y), mass=mass)

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

    def apply_force_by_floats(self, x: float = 0, y: float = 0):
        self.acceleration.x += x / self.mass
        self.acceleration.y += y / self.mass

    def apply_force_nm(self, force: Vector):
        """Applying force without implementing mass"""
        self.acceleration.x += force.x
        self.acceleration.y += force.y

    def apply_forces_list(self, forces: list[Vector]):
        """Applies list of forces upon the object using the formula A = sum(F) / M"""
        # TODO: not sure which one has a better performance
        # self.acceleration.x += sum(f.x for f in forces) / self.mass
        # self.acceleration.y += sum(f.y for f in forces) / self.mass
        for f in forces:
            self.apply_force(f)

    def update(self, game_surface: pygame.Surface, deltatime: float):
        # TODO: implement deltatime
        self.velocity.add(self.acceleration)
        if self.velocity_limit:
            self.velocity.limit(self.velocity_limit)

        self.position.add(self.velocity)
        self.acceleration.set(0, 0)

    def _redraw(self, game_surface: pygame.Surface, deltatime: float, flip_image: bool = False):
        self.current_time += deltatime / 100
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.image_index = (self.image_index + 1) % len(self.images[self.images_key])
            self.current_image = self.images[self.images_key][self.image_index]
        if flip_image:
            game_surface.blit(
                pygame.transform.flip(self.current_image, True, False), (self.position.x, self.position.y))
        else:
            game_surface.blit(self.current_image, (self.position.x, self.position.y))
