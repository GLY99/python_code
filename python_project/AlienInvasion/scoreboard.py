import pygame
import ship


class Scoreboard(object):
    """
    显示得分信息的类
    """
    def __init__(self, ai_game) -> None:
        """
        初始化得分信息
        :param ai_game:
        """
        self.ai_agme = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.setting = ai_game.settings
        self.stats = ai_game.stats
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.score_image = None
        self.score_rect = None
        self.high_score_image = None
        self.high_rect = None
        self.level_image = None
        self.level_rect = None
        self.ships = None
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self) -> None:
        """
        将得分渲染成图像
        :return:
        """
        round_score = round(self.stats.score, -1)
        score_str = "{:,}".format(round_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.setting.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self) -> None:
        """
        在屏幕上显示得分
        :return:
        """
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def prep_high_score(self) -> None:
        """
        在屏幕上显示最高分
        :return:
        """
        high_score = round(self.stats.high_score, -1)
        high_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_str, True, self.text_color, self.setting.bg_color)
        self.high_rect = self.high_score_image.get_rect()
        self.high_rect.centerx = self.screen_rect.centerx
        self.high_rect.top = self.screen_rect.top

    def check_high_score(self) -> None:
        """
        检查是否诞生类新的高分
        :return:
        """
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self) -> None:
        """
        将等级渲染为图像
        :return:
        """
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.setting.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.score_rect.left
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self) -> None:
        """
        绘制飞船剩余数量
        :return:
        """
        self.ships = pygame.sprite.Group()
        for ship_number in range(self.stats.ship_left):
            s = ship.Ship(self.ai_agme)
            s.rect.x = 10 + ship_number * s.rect.width
            s.rect.y = 10
            self.ships.add(s)
