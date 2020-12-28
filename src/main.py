"""
A 2D puzzle game
----------------
optional command line args:
    [-l, -log] {'debug', 'info', 'warning', 'error', 'critical'}
            change logging level    -> default: 'warning'
    [-p, -profile] PROFILE
        using cProfile and output the result into 3 different files
            p_[PROFILE]_output.prof -> cProfile output
            p_[PROFILE]_time.txt    -> sorted by time
            p_[PROFILE]_calls.txt   -> sorted by calls
"""
import pygame

from helper import *
from settings import Settings
from gameclock import GameClock
from gui import GUI
from level import Level


class EzGame:
    logger = logging.getLogger('EzGame')

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        pygame.display.set_mode(
            self.settings.screen_size,
            # pygame.HWSURFACE  # it solves flickering
            # pygame.FULLSCREEN  # crashes my ubuntu :(
        )
        pygame.display.set_caption(self.settings.game_title)
        icon = pygame.image.load('assets/images/icon.png')
        pygame.display.set_icon(icon)

        self.game_clock = GameClock()
        self.game_gui = GUI()

        # TODO: Implement a level manager that calls levels by id
        level_id = 1
        self.current_level = Level(level_id, self.settings, self.game_clock)

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

                if event.key == pygame.K_HOME:
                    self.settings.fps = 60
                if event.key == pygame.K_END:
                    self.settings.fps = 120
                if event.key == pygame.K_BACKQUOTE:
                    self.settings.toggle_show_fps()

                if event.key == pygame.K_p:
                    self.settings.toggle_game_pause()
                if event.key == pygame.K_F11:
                    # TODO: test if the level is being drawn correctly after the toggle
                    pygame.display.toggle_fullscreen()

    def __run(self):
        self.logger.info('Game started running ...')
        while self.game_is_running:
            self.__catch_events()

            # TODO: better implementation of game pause
            if self.settings.is_game_paused:
                continue

            self.current_level.update()
            self.game_gui.update(self.settings.show_fps, self.game_clock.fps)
            pygame.display.flip()


if __name__ == '__main__':
    args = parse_cl_args()

    logging.basicConfig(
        format='%(name)13s %(levelname)7s: %(message)s',
        level=getattr(logging, args.loglevel.upper())
    )
    logger = logging.getLogger('Main')
    logger.info('Starting the game ...')

    if not args.profile:
        EzGame()
    else:
        profile_game(args.profile)
