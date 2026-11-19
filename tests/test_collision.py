import os
import unittest

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")

import pygame

from game.bullet import Bullet
from game.game_engine import GameEngine


class CollisionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pygame.init()
        pygame.display.set_mode((1, 1))

    @classmethod
    def tearDownClass(cls):
        pygame.quit()

    def test_simultaneous_bullet_collisions_score_each_enemy_once(self):
        engine = GameEngine(600, 700)
        engine.enemy_fire_chance = 0
        enemies = engine.enemy_grid.alive_enemies()[:2]
        engine.player_bullets = [Bullet(enemy.x, enemy.y + 18, speed=0) for enemy in enemies]

        engine.update()

        self.assertEqual(engine.score, 2)
        self.assertEqual(len(engine.player_bullets), 0)
        self.assertFalse(any(enemy.alive for enemy in enemies))


if __name__ == "__main__":
    unittest.main()
