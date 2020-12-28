import logging
import pygame


class GUI:
    logger = logging.getLogger('GUI')

    def __init__(self):
        self.fonts = self.__load_fonts()
        self.fps_pos = 5, 5

    def __load_fonts(self):
        fonts = {'fps': pygame.font.SysFont("Arial", 17)}
        self.logger.info("Fonts are loaded")
        return fonts

    def show_fps(self, game_surface: pygame.Surface, fps: float):
        fps_str = str(int(fps))
        fps_txt = self.fonts['fps'].render(fps_str, True, pygame.Color("coral"))
        game_surface.blit(fps_txt, self.fps_pos)

    def update(self, show_fps: bool, fps: float):
        if show_fps:
            game_surface = pygame.display.get_surface()
            self.show_fps(game_surface, fps)
