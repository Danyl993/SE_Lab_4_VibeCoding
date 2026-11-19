import os
import unittest

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")

import pygame

from game.bullet import Bullet
from game.game_engine import GameEngine


class GameOverTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pygame.init()
        pygame.display.set_mode((1, 1))

    @classmethod
    def tearDownClass(cls):
        pygame.quit()

    def setUp(self):
        self.engine = GameEngine(600, 700)
        self.engine.enemy_fire_chance = 0

    def test_enemy_bullet_hit_ends_round_and_keeps_score(self):
        self.engine.score = 7
        self.engine.enemy_bullets = [Bullet(self.engine.player.x, self.engine.player.y - 5, direction=1)]
        self.engine.update()
        self.assertTrue(self.engine.game_over)
        self.assertEqual(self.engine.score, 7)

    def test_enemy_grid_at_player_line_ends_round(self):
        enemy = self.engine.enemy_grid.alive_enemies()[0]
        enemy.y = self.engine.player.y - enemy.height
        self.engine.update()
        self.assertTrue(self.engine.game_over)

    def test_game_over_screen_renders(self):
        self.engine.game_over = True
        surface = pygame.Surface((600, 700))
        self.engine.render(surface)
        self.assertIsInstance(surface, pygame.Surface)


if __name__ == "__main__":
    unittest.main()
