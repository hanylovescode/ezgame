import pygame


class GUI:
    def __init__(self, font: pygame.font.Font):
        self.font = font
        self.fps_pos = 5, 5

    def show_fps(self, game_surface: pygame.Surface, fps: float):
        fps_str = str(int(fps))
        fps_txt = self.font.render(fps_str, True, pygame.Color("coral"))
        game_surface.blit(fps_txt, self.fps_pos)

    def update(self, game_surface: pygame.Surface, show_fps: bool, fps: float):
        if show_fps:
            self.show_fps(game_surface, fps)
