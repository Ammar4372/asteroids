from typing import Any
import pygame


class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius) -> None:
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
    def detect_collision(self, opponent: object):
        distance = self.position.distance_to(opponent.position)
        sum = self.radius + opponent.radius
        if distance > sum:
            return False
        return True
