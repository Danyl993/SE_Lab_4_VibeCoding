import os
import unittest

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")

import pygame

from game.game_engine import GameEngine


class ReplayTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pygame.init()
        pygame.display.set_mode((1, 1))

    @classmethod
    def tearDownClass(cls):
        pygame.quit()

    def test_difficulty_restarts_a_clean_round(self):
        engine = GameEngine(600, 700)
        engine.score = 12
        engine.game_over = True
        engine.handle_event(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_3))
        self.assertEqual(engine.difficulty, "hard")
        self.assertFalse(engine.game_over)
        self.assertEqual(engine.score, 0)
        self.assertEqual(len(engine.enemy_grid.alive_enemies()), 32)
        self.assertAlmostEqual(engine.enemy_grid.speed, 2.2)

    def test_space_fires_and_q_exits_game_over(self):
        engine = GameEngine(600, 700)
        engine.handle_event(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_SPACE))
        self.assertEqual(len(engine.player_bullets), 1)
        engine.game_over = True
        self.assertEqual(
            engine.handle_event(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_q)), "quit"
        )


if __name__ == "__main__":
    unittest.main()
