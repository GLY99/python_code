import sys
import time
from typing import Any
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


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
        self.settings = Settings()
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion(Enter 'Q' exit)")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self.stats = GameStats(self)
        self.play_button = Button(self, "Play")
        self.sb = Scoreboard(self)

    def run_game(self) -> None:
        """
        开始游戏的主循环
        :return:
        """
        while True:
            self._check_event()
            if self.stats.game_activate:
                self.ship.update()
                self._update_bullet()
                self._update_alien()
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

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
        self.aliens.draw(self.screen)
        if not self.stats.game_activate:
            self.play_button.draw_button()
        self.sb.show_score()
        # 让最近录制的屏幕可见
        pygame.display.flip()

    def _check_keydown_events(self, event: Any) -> None:
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
            self.stats.write_high_score_to_file()
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_UP:
            self.ship.moveing_up = True
        elif event.key ==pygame.K_DOWN:
            self.ship.moveing_down = True

    def _check_keyup_events(self, event: Any) -> None:
        """
        响应键盘抬起
        :param event:
        :return:
        """
        if event.key == pygame.K_RIGHT:
            self.ship.moveing_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moveing_left = False
        elif event.key == pygame.K_UP:
            self.ship.moveing_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moveing_down = False

    def _fire_bullet(self) -> None:
        """
        创建子弹
        :return:
        """
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
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
        self._check_bullet_alien_collections()

    def _check_bullet_alien_collections(self) -> None:
        """
        检查子弹和外星人碰撞
        :return:
        """
        collects = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collects:
            for aliens in collects.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            self.stats.level += 1
            self.sb.prep_level()

    def _create_fleet(self) -> None:
        """
        创建外星人群
        :return:
        """
        al = Alien(self)
        al_width, al_height = al.rect.size
        ship_height = self.ship.rect.height
        available_space_x = self.settings.screen_width - (2 * al_width)
        available_space_y = (
            self.settings.screen_height - (3 * al_height) - ship_height
        )
        number_aliens_x = available_space_x // (2 * al_width)
        number_rows = available_space_y // (2 * al_height)
        # 创建外星人群
        for row in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row)

    def _create_alien(self, alien_number: int, row: int) -> None:
        """
        创建一个外星人并且将其放在当前行
        :return:
        """
        al = Alien(self)
        al_width, al_height = al.rect.size
        al.x = al_width + 2 * al_width * alien_number
        al_y = al_height + 2 * al_height * row
        al.rect.x = al.x
        al.rect.y = al_y
        self.aliens.add(al)

    def _update_alien(self) -> None:
        """
        更新外星人位置
        :return:
        """
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_alien_bottom()

    def _check_fleet_edges(self) -> None:
        """
        有外星人移动到边缘采取相应的措施
        :return:
        """
        for al in self.aliens:
            if al.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self) -> None:
        """
        将外星人群下移，并且改变方向
        :return:
        """
        for al in self.aliens:
            al.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self) -> None:
        """
        响应飞船被外星人撞到
        :return:
        """
        if self.stats.ship_left > 0:
            self.stats.ship_left -= 1
            self.sb.prep_ships()
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()
            time.sleep(0.5)
        else:
            self.stats.game_activate = False
            pygame.mouse.set_visible(True)

    def _check_alien_bottom(self) -> None:
        """
        检查外星人到了屏幕底部
        :return:
        """
        screen_rect = self.screen.get_rect()
        for al in self.aliens.sprites():
            if al.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _check_play_button(self, mouse_pos) -> None:
        """
        在单击play时开始游戏
        :param mouse_pos:
        :return:
        """
        if self.play_button.rect.collidepoint(mouse_pos) and not self.stats.game_activate:
            self.settings.initialize_dynamic_setting()
            self.stats.reset_stats()
            self.stats.game_activate = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            # 清空余下的外星人和子弹
            self.aliens.empty()
            self.bullets.empty()
            # 创建一群新的外星人和飞船
            self._create_fleet()
            self.ship.center_ship()
            pygame.mouse.set_visible(False)


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
