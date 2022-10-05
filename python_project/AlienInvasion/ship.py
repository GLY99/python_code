import pygame


class Ship(object):
    """
    管理飞船的类
    """
    def __init__(self, ai_game) -> None:
        """
        初始化飞船并且设置位置
        """
        self.setting = ai_game.settings
        self.screen = ai_game.screen
        # 获取屏幕的外接矩形
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并且获取其外接矩形
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # 对于每个新飞船都将其放在屏幕底部中央
        self.rect.midbottom = self.screen_rect.midbottom

        # 在飞船的属性x中存储小数
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # 移动标志
        self.moveing_right = False
        self.moveing_left = False
        self.moveing_up = False
        self.moveing_down = False

    def blitem(self) -> None:
        """
        在指定位置绘制飞船
        :return:
        """
        self.screen.blit(self.image, self.rect)

    def update(self) -> None:
        """
        更新飞船位置
        :return:
        """
        if self.moveing_right and self.rect.right < self.screen_rect.right:
            self.x += self.setting.ship_speed
        if self.moveing_left and self.rect.left > 0:
            self.x -= self.setting.ship_speed
        if self.moveing_up and self.rect.top > 0:
            self.y -= self.setting.ship_speed
        if self.moveing_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.setting.ship_speed
        self.rect.x = self.x
        self.rect.y = self.y

    def center_ship(self) -> None:
        """
        让飞船居中
        :return:
        """
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
