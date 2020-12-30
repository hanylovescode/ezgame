import logging
import pygame

from src.gameclock import GameClock
from src.vector import Vector


class Walker:
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


class Mouse:
    def __init__(self):
        self.position = Vector(0, 0)

    def update(self):
        self.position.x, self.position.y = pygame.mouse.get_pos()


class Scratch:
    logger = logging.getLogger('TestClass')

    def __init__(self):
        pygame.init()
        pygame.display.set_mode((800, 600))

        self.game_clock = GameClock()

        self.mouse = Mouse()

        self.walker = Walker(Vector(400, 300), Vector(0, 0))

        self.game_is_running = True
        self.__run()

    def __catch_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.logger.warning('Game was forced to close!')
                self.game_is_running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game_is_running = False
                    self.logger.info('Game closed.')

    def __update(self):
        game_surface = pygame.display.get_surface()
        game_surface.fill((0, 0, 0))

        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.walker.update(mouse_x, mouse_y)

        self.walker.redraw(game_surface)

        pygame.display.flip()

    def __run(self):
        while self.game_is_running:
            self.__catch_events()
            self.game_clock.update(120)
            self.__update()
        pygame.quit()


if __name__ == '__main__':
    logging.basicConfig(
        format='%(name)13s %(levelname)7s: %(message)s',
        level="INFO"
    )
    Scratch()
