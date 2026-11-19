import os
import unittest

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")

import pygame

from game.game_engine import GameEngine


class SoundTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pygame.init()
        pygame.display.set_mode((1, 1))

    @classmethod
    def tearDownClass(cls):
        pygame.quit()

    def test_sound_effects_exist_or_game_runs_silently(self):
        engine = GameEngine(600, 700)
        self.assertTrue(set(engine._sounds).issubset({"shoot", "destroy", "game_over"}))
        engine._play_sound("shoot")
        engine._play_sound("destroy")
        engine._play_sound("game_over")


if __name__ == "__main__":
    unittest.main()
