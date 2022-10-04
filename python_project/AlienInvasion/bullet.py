import pygame
from pygame import sprite


class Bullet(sprite.Sprite):
    """
    管理子弹发射的类
    """
    def __init__(self, ai_game) -> None:
        """
        在飞船的当前位置创建一个子弹
        """
        super(Bullet, self).__init__()
        self.screen = ai_game.screen
        self.setting = ai_game.settings
        self.color = self.setting.bullet_color

        # 在（0， 0）创建一个表示子弹的矩形， 再设置正确的位置
        self.rect = pygame.Rect(0, 0, self.setting.bullet_width, self.setting.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # 子弹只会在y方向移动
        self.y = float(self.rect.y)

    def update(self) -> None:
        """
        更新子弹信息
        :return:
        """
        self.y -= self.setting.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self) -> None:
        """
        绘制子弹
        :return:
        """
        pygame.draw.rect(self.screen, self.color, self.rect)