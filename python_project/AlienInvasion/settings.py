class Settings(object):
    """
    存储游戏中所有设置的类
    """
    def __init__(self) -> None:
        """
        初始化游戏设置
        """
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 2.0
        self.ship_limit = 3
        self.bullet_speed = 3.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        self.speed_scale = 1.1
        self.alien_points = 50
        self.socre_scale = 2
        self.bullet_allowed_scale = 2
        self.initialize_dynamic_setting()

    def initialize_dynamic_setting(self) -> None:
        """
        初始化随游戏进行而变化的设置
        :return:
        """
        self.ship_speed = 2.0
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self) -> None:
        """
        提高速度设置
        :return:
        """
        self.ship_speed *= self.speed_scale
        self.bullet_speed *= self.speed_scale
        self.alien_speed *= self.speed_scale
        self.alien_points *= self.socre_scale
        self.bullet_allowed *= self.bullet_allowed_scale
