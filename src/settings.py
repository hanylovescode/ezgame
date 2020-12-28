import pygame
import logging


class Settings:
    logger = logging.getLogger("Settings")

    def __init__(self):
        self.game_title: str = "EZgame"
        self.screen_size = 1280, 720
        # self.background_color = (0, 0, 0)
        self.background_color = (34, 31, 49)  # Not sure if black was better

        self.is_game_paused = False
        self.show_fps = True
        self.__fps = 120

    def toggle_game_pause(self):
        self.is_game_paused = not self.is_game_paused

    def toggle_show_fps(self):
        self.show_fps = not self.show_fps

    @property
    def fps(self) -> int:
        return self.__fps

    @fps.setter
    def fps(self, val: int):
        if 60 <= val <= 120:
            self.__fps = val
            self.logger.info(f"fps changed to {self.__fps}")
