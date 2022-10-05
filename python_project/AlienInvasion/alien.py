from typing import Any
import pygame
from pygame import sprite


class Alien(sprite.Sprite):
    """
    单个外星人类
    """
    def __init__(self, ai_game) -> None:
        """
        初始化外星人并且设置初始位置
        """
        super(Alien, self).__init__()
        self.screen = ai_game.screen
        # 加载外星人设置rect属性
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()
        # 设置每个外星人最开始都在屏幕上方
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # 记录外星人的水平位置
        self.x = float(self.rect.x)
        self.setting = ai_game.settings

    def update(self, *args: Any, **kwargs: Any) -> None:
        """
        更新外星人位置
        :param args:
        :param kwargs:
        :return:
        """
        self.x += self.setting.alien_speed * self.setting.fleet_direction
        self.rect.x = self.x

    def check_edges(self) -> bool:
        """
        检查外星人是否撞到了边缘
        :return:
        """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
        return False
