import pygame
import random

from scripts.player import Player

class Borgar:
    def __init__(self):
        self.surface: pygame.Surface = pygame.image.load("assets/borgar.png").convert()
        self.surface.set_colorkey("white")

        self.position_x = 130
        self.position_y = 130

        self.hitbox: pygame.Rect = pygame.Rect(self.position_x, self.position_y, 8, 8)

        self.fall_speed = 50
    
    def reset(self):
        self.position_x = 130
        self.position_y = 130

        self.hitbox.left = self.position_x
        self.hitbox.top = self.position_y
    
    def update(self, delta_time):
        self.position_y += self.fall_speed * delta_time

        self.hitbox.left = self.position_x
        self.hitbox.top = self.position_y

    def draw(self, screen: pygame.Surface):
        screen.blit(self.surface, dest=(self.position_x, self.position_y))
    
    def is_colliding_player(self, player: Player):
        return self.hitbox.colliderect(player.hitbox)

    def spawn(self):
        self.position_x = random.randrange(0, 121)
        self.position_y = 0
    
    def is_out_of_bounds(self):
        return self.position_y > 128

class BorgarPool:
    def __init__(self):
        self.borgars = [Borgar() for i in range(7)]
    
    def spawn_borgar(self) -> None:
        for borgar in self.borgars:
            if not borgar.is_out_of_bounds():
                continue

            borgar.spawn()
            break
    
    def reset_all(self):
        for borgar in self.borgars:
            borgar.reset()
    
    def update_all(self, delta_time):
        for borgar in self.borgars:
            if borgar.is_out_of_bounds():
                continue

            borgar.update(delta_time)
    
    def draw_all(self, screen):
        for borgar in self.borgars:
            if borgar.is_out_of_bounds():
                continue

            borgar.draw(screen)
    
    def are_colliding_player(self, player):
        for borgar in self.borgars:
            if borgar.is_colliding_player(player):
                borgar.position_y = 200
                borgar.hitbox.top = 200
                return True
        
        return False