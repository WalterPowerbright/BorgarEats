# /// script
# dependencies = [
# "pygame-ce"
# ]

import asyncio

import pygame

from scripts.player import Player
from scripts.game import Game

import sys
if sys.platform in ['wasm', 'emscripten']:
    from platform import window
    window.canvas.style.imageRendering = 'pixelated'

if __name__ == "__main__":
    game = Game()
    asyncio.run(game.main_loop())