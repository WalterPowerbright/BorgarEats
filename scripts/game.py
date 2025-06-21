import pygame, asyncio
from enum import Enum

from scripts.constants import *

from scripts.player import Player
from scripts.borgar import BorgarPool
from scripts.timer import Timer
from scripts.ui import UserInterface, TitleScreen, EndScreen

class GameState(Enum):
    START = 0
    PLAYING = 1
    END = 2

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((128, 128))
        self.clock = pygame.time.Clock()
        self.running = True
        self.delta_time = 0

        self.player = Player()
        self.borgar_pool = BorgarPool()

        self.spawn_timer = Timer(0.3)

        self.duration_timer = Timer(1.0)
        self.GAME_DURATION = 30
        self.current_duration = self.GAME_DURATION

        self.score = 0
        self.final_score = self.score

        self.current_state = GameState.START

        self.user_interface = UserInterface()
        self.title = TitleScreen()
        self.ending = EndScreen()
    
    def check_game_should_close(self, event_list):
        for event in event_list:
            if event.type == pygame.QUIT:
                self.running = False
    
    def handle_spawn_timer(self):
        self.spawn_timer.update(delta_time=self.delta_time)
        if self.spawn_timer.is_timeout():
           self.spawn_timer.reset()
           self.borgar_pool.spawn_borgar()
    
    def handle_duration_timer(self):
        self.duration_timer.update(delta_time=self.delta_time)
        if self.duration_timer.is_timeout():
            self.duration_timer.reset()
            self.current_duration -= 1

    def reset_game(self):
        self.player.reset()
        self.borgar_pool.reset_all()
        self.spawn_timer.reset()
        self.duration_timer.reset()
        self.current_duration = self.GAME_DURATION
        self.score = 0

    def run_gameplay(self):
        self.handle_spawn_timer()
        self.handle_duration_timer()

        self.player.update(delta_time=self.delta_time)
        self.borgar_pool.update_all(delta_time=self.delta_time)

        if self.borgar_pool.are_colliding_player(player=self.player):
            self.score += 1

        self.player.draw(self.screen)
        self.borgar_pool.draw_all(self.screen)
        self.user_interface.draw(screen=self.screen, score=self.score, time_left=self.current_duration)

    async def main_loop(self):
        while self.running:
            event_list = pygame.event.get()
            self.check_game_should_close(event_list)
        
            self.screen.fill(NOKIA_LIGHT)

            if self.current_state is GameState.START:
                self.title.draw(screen=self.screen)
            elif self.current_state is GameState.PLAYING:
                self.run_gameplay()
            elif self.current_state is GameState.END:
                self.ending.draw(final_score=self.final_score, screen=self.screen)
            
            for event in event_list:
                if event.type == pygame.KEYDOWN and (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                    if self.current_state is GameState.START:
                        self.current_state = GameState.PLAYING
                    elif self.current_state is GameState.END:
                        self.current_state = GameState.START

            if self.current_duration <= 0:
                self.final_score = self.score
                self.reset_game()
                self.current_state = GameState.END

            pygame.display.flip()

            self.delta_time = self.clock.tick(60) / 1000
            await asyncio.sleep(0)
        
        pygame.quit()