import sys
import pygame

import settings
import ship
import bullet


class AlienInvasion(object):
    """
    管理游戏资源和行为的类
    """
    def __init__(self) -> None:
        """
        初始化游戏并且创建游戏资源
        """
        super(AlienInvasion, self).__init__()
        pygame.init()
        self.settings = settings.Settings()
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion(Enter 'Q' exit)")
        self.ship = ship.Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self) -> None:
        """
        开始游戏的主循环
        :return:
        """
        while True:
            self._check_event()
            self.ship.update()
            self._update_bullet()
            self._update_screen()

    def _check_event(self) -> None:
        """
        check event
        :return:
        """
        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _update_screen(self) -> None:
        """
        update screen
        :param self:
        :return:
        """
        # 每次循环都重新绘制屏幕
        self.screen.fill(self.settings.bg_color)
        self.ship.blitem()
        for bul in self.bullets.sprites():
            bul.draw_bullet()
        # 让最近录制的屏幕可见
        pygame.display.flip()

    def _check_keydown_events(self, event) -> None:
        """
        响应键盘按下
        :param event:
        :return:
        """
        if event.key == pygame.K_RIGHT:
            self.ship.moveing_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moveing_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event) -> None:
        """
        响应键盘抬起
        :param event:
        :return:
        """
        if event.key == pygame.K_RIGHT:
            self.ship.moveing_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moveing_left = False

    def _fire_bullet(self) -> None:
        """
        创建子弹
        :return:
        """
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = bullet.Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullet(self) -> None:
        """
        更新子弹
        :return:
        """
        self.bullets.update()
        for bul in self.bullets.copy():
            if bul.rect.bottom <= 0:
                self.bullets.remove(bul)
        print(len(self.bullets))


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
