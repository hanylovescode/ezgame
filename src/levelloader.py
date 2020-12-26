import pygame
import logging


class LevelLoader:
    logger = logging.getLogger("LevelLoader")

    def __init__(self):
        self.file = self.load_file()
        self.fonts = self.load_fonts()
        self.images = self.load_images()
        self.sounds = self.load_sounds()

    def load_file(self):
        # TODO: load file
        self.logger.info("File is loaded")
        return []

    def load_fonts(self):
        fonts = [pygame.font.SysFont("Arial", 17)]
        self.logger.info("Fonts are loaded")
        return fonts

    def load_images(self):
        # TODO: load images
        self.logger.info("Images are loaded")
        return []

    @staticmethod
    def load_image(image_path: str, with_alpha: bool = True):
        if with_alpha:
            return pygame.image.load(image_path).convert_alpha()
        return pygame.image.load(image_path).convert()

    def load_sounds(self):
        # TODO: load sounds
        self.logger.info("Sounds are loaded")
        return []
