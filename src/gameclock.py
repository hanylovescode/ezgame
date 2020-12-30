import time

import pygame


class GameClock:
    def __init__(self):
        self.__clock = pygame.time.Clock()
        self.__last_frame = time.time()
        self.__deltatime = 1

    @property
    def fps(self):
        return self.__clock.get_fps()

    @property
    def deltatime(self):
        return self.__deltatime

    def __update_delta_time(self):
        current_frame = time.time()
        self.__deltatime = (current_frame - self.__last_frame) * 100
        self.__last_frame = current_frame

    def update(self, fps_value):
        self.__update_delta_time()
        self.__clock.tick(fps_value)
