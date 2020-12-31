import logging
from enum import IntFlag, auto

import pygame

from src.gameclock import GameClock
from src.vector import Vector
from experiments.walker import Walker


class State(IntFlag):
    FACING_RIGHT = auto()
    FACING_LEFT = auto()
    MOVING = auto()
    JUMPING = auto()
    FALLING = auto()


class Scratch:
    logger = logging.getLogger('TestClass')

    def __init__(self):
        pygame.init()
        pygame.display.set_mode((800, 600))

        self.game_clock = GameClock()

        self.gravity = Vector(0, 1)
        self.wind = Vector(10, 0)
        self.jump_force = Vector(0, -20)
        self.__moving_right_force = Vector()
        self.__moving_left_force = Vector()
        self.moving_magnitude = 0.1

        self.state = State.FACING_RIGHT

        self.walker = Walker(Vector(400, 300), mass=1)
        # self.walker.velocity_limit = 5

        self.game_is_running = True
        self.__run()

    @property
    def moving_magnitude(self):
        return self.__moving_magnitude

    @moving_magnitude.setter
    def moving_magnitude(self, value: float):
        self.__moving_magnitude = value
        self.__moving_right_force.x = value
        self.__moving_left_force.x = -value

    def __bound_to_ground(self):
        if self.walker.position.y >= 540:
            self.walker.position.y = 540
            self.walker.velocity.y = 0
            self.state &= ~State.JUMPING

    def __catch_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.logger.warning('Game was forced to close!')
                self.game_is_running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game_is_running = False
                    self.logger.info('Game closed.')

        keys = pygame.key.get_pressed()
        if State.JUMPING not in self.state:
            if keys[pygame.K_SPACE] or keys[pygame.K_w]:
                self.walker.apply_force(self.jump_force)
                self.state |= State.JUMPING

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.walker.apply_force(self.__moving_right_force)
            # TODO: learn how to combine the two lines below
            self.state |= State.MOVING | State.FACING_RIGHT
            self.state &= ~State.FACING_LEFT
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.walker.apply_force(self.__moving_left_force)
            self.state |= State.MOVING | State.FACING_LEFT
            self.state &= ~State.FACING_RIGHT
        else:
            self.state &= ~State.MOVING

    def __update(self):
        game_surface = pygame.display.get_surface()
        game_surface.fill((0, 0, 0))

        # mouse_x, mouse_y = pygame.mouse.get_pos()

        self.walker.apply_force(self.gravity)
        self.walker.update()
        self.__bound_to_ground()

        self.walker.redraw(game_surface)

        pygame.display.flip()

    def __run(self):
        while self.game_is_running:
            self.game_clock.update(120)
            self.__catch_events()
            self.__update()
            self.logger.info(f'state: {self.state}')
        pygame.quit()


if __name__ == '__main__':
    logging.basicConfig(
        format='%(name)13s %(levelname)7s: %(message)s',
        level="INFO"
    )
    Scratch()
