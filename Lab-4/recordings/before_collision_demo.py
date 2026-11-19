"""Show the untouched starter's skipped-bullet collision bug reproducibly."""

import sys
from pathlib import Path

BASELINE_SOURCE = Path(__file__).parent / "before-source"
sys.path.insert(0, str(BASELINE_SOURCE))

import pygame

from game.bullet import Bullet
from game.game_engine import GameEngine


def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 700))
    pygame.display.set_caption("Lab 4 - Untouched Starter Collision Bug")
    clock = pygame.time.Clock()

    engine = GameEngine(600, 700)
    engine.enemy_fire_chance = 0
    first_two_enemies = engine.enemy_grid.alive_enemies()[:2]
    engine.player_bullets = [
        Bullet(enemy.x, enemy.y + 18, speed=0) for enemy in first_two_enemies
    ]
    engine.update()

    heading = pygame.font.SysFont("Arial", 22, bold=True)
    note = pygame.font.SysFont("Arial", 18)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key in (pygame.K_q, pygame.K_ESCAPE)
            ):
                running = False

        screen.fill((0, 0, 0))
        engine.render(screen)
        screen.blit(heading.render("Starter collision bug reproduction", True, (255, 215, 80)), (10, 45))
        screen.blit(note.render("Two bullets overlap two enemies on one frame.", True, (255, 255, 255)), (10, 73))
        screen.blit(note.render("Expected score: 2   |   Actual score: 1", True, (255, 100, 100)), (10, 99))
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
