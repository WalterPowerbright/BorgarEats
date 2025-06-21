import pygame

from scripts.constants import *

class UserInterface:
    def __init__(self):
        self.border: pygame.Surface = pygame.Surface((128, 26))
        self.border.fill(NOKIA_DARK)
        self.font: pygame.font.Font = pygame.font.Font("assets/silkscreen.ttf", 8)
    
    def get_score_text(self, score: int) -> str:
        return "Score: " + str(score)
    
    def get_time_text(self, time_left: int) -> str:
        return "Time: " + str(time_left)

    def draw(self, screen: pygame.Surface, score: int, time_left: int):
        score_text: pygame.Surface = self.font.render(self.get_score_text(score), False, NOKIA_LIGHT)
        time_text: pygame.Surface = self.font.render(self.get_time_text(time_left), False, NOKIA_LIGHT)

        screen.blit(self.border, (0, 0))
        screen.blit(score_text, (2,2))
        screen.blit(time_text, (2,12))

class TitleScreen:
    def __init__(self):
        self.title_font: pygame.font.Font = pygame.font.Font("assets/silkscreen-bold.ttf", 16)
        self.instructions_font: pygame.font.Font = pygame.font.Font("assets/silkscreen.ttf", 8)

        self.title_text: pygame.Surface = self.title_font.render("BORGAR\nEATS", False, NOKIA_DARK)
        self.instructions_text: pygame.Surface = self.instructions_font.render("Press <- or ->\nto START", False, NOKIA_DARK)
    
    def draw(self, screen: pygame.Surface):
        screen.blit(self.title_text, (8,16))
        screen.blit(self.instructions_text, (9,66))

class EndScreen:
    def __init__(self):
        self.time_up_font: pygame.font.Font = pygame.font.Font("assets/silkscreen-bold.ttf", 16)
        self.text_font: pygame.font.Font = pygame.font.Font("assets/silkscreen.ttf", 8)
        self.bold_font: pygame.font.Font = pygame.font.Font("assets/silkscreen-bold.ttf", 8)

        self.time_up_text: pygame.Surface = self.time_up_font.render("TIME'S\nUP!", False, NOKIA_DARK)
        self.instructions_text: pygame.Surface = self.bold_font.render("Press <- or ->\nto RESET", False, NOKIA_DARK)
    
    def draw(self, final_score: int, screen: pygame.Surface):
        score_string: str = "Score: " + str(final_score)
        self.score_text: pygame.Surface = self.text_font.render(score_string, False, NOKIA_DARK)

        screen.blit(self.time_up_text, (8,16))
        screen.blit(self.score_text, (9,66))
        screen.blit(self.instructions_text, (9,84))