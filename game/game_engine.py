import math
import random
from array import array

import pygame

from .bullet import Bullet
from .enemy import EnemyGrid
from .player import Player

WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (220, 60, 60)
YELLOW = (255, 215, 80)


class GameEngine:
    """Owns a game round and its menu, collision, and sound behavior."""

    DIFFICULTIES = {
        "easy": {"speed": 1.0, "fire_chance": 0.004},
        "medium": {"speed": 1.5, "fire_chance": 0.01},
        "hard": {"speed": 2.2, "fire_chance": 0.018},
    }
    DIFFICULTY_KEYS = {
        pygame.K_1: "easy",
        pygame.K_2: "medium",
        pygame.K_3: "hard",
    }

    def __init__(self, width, height, difficulty="medium"):
        self.width = width
        self.height = height
        self.font = pygame.font.SysFont("Arial", 30)
        self.title_font = pygame.font.SysFont("Arial", 42, bold=True)
        self._sounds = self._create_sounds()
        self.difficulty = difficulty if difficulty in self.DIFFICULTIES else "medium"
        self._reset_round()

    def _create_sounds(self):
        """Create short effects in memory; play silently if audio is unavailable."""
        sounds = {}
        try:
            if not pygame.mixer.get_init():
                pygame.mixer.init(frequency=22050, size=-16, channels=1, buffer=512)
            sample_rate = 22050
            for name, frequency, duration in (
                ("shoot", 720, 0.07),
                ("destroy", 240, 0.14),
                ("game_over", 110, 0.35),
            ):
                count = int(sample_rate * duration)
                samples = array(
                    "h",
                    (
                        int(7000 * (1 - index / count) * math.sin(2 * math.pi * frequency * index / sample_rate))
                        for index in range(count)
                    ),
                )
                sounds[name] = pygame.mixer.Sound(buffer=samples.tobytes())
        except pygame.error:
            # Headless systems may not have an audio device. Game logic stays usable.
            return {}
        return sounds

    def _play_sound(self, name):
        sound = self._sounds.get(name)
        if sound:
            try:
                sound.play()
            except pygame.error:
                pass

    def _reset_round(self):
        settings = self.DIFFICULTIES[self.difficulty]
        self.player = Player(self.width // 2 - 20, self.height - 50, 40, 20)
        self.enemy_grid = EnemyGrid(self.width, speed=settings["speed"])
        self.enemy_fire_chance = settings["fire_chance"]
        self.player_bullets = []
        self.enemy_bullets = []
        self._shoot_cooldown = 0
        self.score = 0
        self.game_over = False

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            return "quit"

        if event.type != pygame.KEYDOWN:
            return None

        if self.game_over:
            if event.key in self.DIFFICULTY_KEYS:
                self.difficulty = self.DIFFICULTY_KEYS[event.key]
                self._reset_round()
            elif event.key in (pygame.K_q, pygame.K_ESCAPE):
                return "quit"
            return None

        if event.key == pygame.K_SPACE and self._shoot_cooldown <= 0:
            bullet_x = self.player.center_x() - 2
            self.player_bullets.append(Bullet(bullet_x, self.player.y, direction=-1))
            self._shoot_cooldown = 15
            self._play_sound("shoot")
        return None

    def handle_input(self):
        if self.game_over:
            return
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.player.move(-self.player.speed, self.width)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.player.move(self.player.speed, self.width)

    def _end_round(self):
        if not self.game_over:
            self.game_over = True
            self._play_sound("game_over")

    def update(self):
        if self.game_over:
            return

        if self._shoot_cooldown > 0:
            self._shoot_cooldown -= 1

        self.enemy_grid.move()
        for enemy in self.enemy_grid.alive_enemies():
            if random.random() < self.enemy_fire_chance:
                bullet_x = enemy.x + enemy.width // 2
                self.enemy_bullets.append(Bullet(bullet_x, enemy.y + enemy.height, direction=1))

        for bullet in self.player_bullets:
            bullet.move()
        for bullet in self.enemy_bullets:
            bullet.move()

        self.player_bullets = [b for b in self.player_bullets if not b.off_screen(self.height)]
        self.enemy_bullets = [b for b in self.enemy_bullets if not b.off_screen(self.height)]

        # Build a survivor list instead of removing from a list being iterated.
        # Each player bullet can hit at most one enemy, and dead enemies are
        # excluded immediately so simultaneous bullets cannot score twice.
        alive_enemies = self.enemy_grid.alive_enemies()
        surviving_bullets = []
        for bullet in self.player_bullets:
            hit_enemy = next(
                (enemy for enemy in alive_enemies if bullet.rect().colliderect(enemy.rect())),
                None,
            )
            if hit_enemy is None:
                surviving_bullets.append(bullet)
                continue
            hit_enemy.alive = False
            alive_enemies.remove(hit_enemy)
            self.score += 1
            self._play_sound("destroy")
        self.player_bullets = surviving_bullets

        if any(bullet.rect().colliderect(self.player.rect()) for bullet in self.enemy_bullets):
            self._end_round()
        elif self.enemy_grid.reached_bottom(self.player.y):
            self._end_round()

    def _draw_centered(self, screen, text, y, color=WHITE, font=None):
        image = (font or self.font).render(text, True, color)
        screen.blit(image, image.get_rect(center=(self.width // 2, y)))

    def render(self, screen):
        pygame.draw.rect(screen, GREEN, self.player.rect())

        for enemy in self.enemy_grid.alive_enemies():
            pygame.draw.rect(screen, WHITE, enemy.rect())

        for bullet in self.player_bullets:
            pygame.draw.rect(screen, WHITE, bullet.rect())
        for bullet in self.enemy_bullets:
            pygame.draw.rect(screen, RED, bullet.rect())

        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        if self.game_over:
            overlay = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 205))
            screen.blit(overlay, (0, 0))
            self._draw_centered(screen, "GAME OVER", self.height // 2 - 105, RED, self.title_font)
            self._draw_centered(screen, f"Final score: {self.score}", self.height // 2 - 45)
            self._draw_centered(screen, "Choose a difficulty to play again", self.height // 2 + 15, YELLOW)
            self._draw_centered(screen, "1  Easy     2  Medium     3  Hard", self.height // 2 + 60)
            self._draw_centered(screen, "Q or Esc  Exit", self.height // 2 + 105)
