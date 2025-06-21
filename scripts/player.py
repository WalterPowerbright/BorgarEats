import pygame

class Player:
    def __init__(self):
        self.surface = pygame.image.load("assets/big-mouth.png").convert()
        self.surface.set_colorkey("white")

        self.position_x = 60
        self.position_y = 112
        self.hitbox: pygame.Rect = pygame.Rect(self.position_x, self.position_y, 8, 8)

        self.move_speed = 100
    
    def reset(self):
        self.position_x = 60
        self.position_y = 114

        self.hitbox.left = self.position_x
        self.hitbox.top = self.position_y
    
    def update(self, delta_time):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.position_x -= self.move_speed * delta_time
        if keys[pygame.K_RIGHT]:
            self.position_x += self.move_speed * delta_time
        
        self.position_x = 0 if self.position_x < 0 else 120 if self.position_x > 120 else self.position_x
        
        self.hitbox.left = self.position_x
        self.hitbox.top = self.position_y

    def draw(self, screen):
        screen.blit(self.surface, (self.position_x, self.position_y))