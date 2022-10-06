class GameStats(object):
    """
    跟踪游戏的统计信息
    """
    def __init__(self, ai_game) -> None:
        """
        初始化统计信息
        """
        self.setting = ai_game.settings
        self.ship_left = 0
        self.reset_stats()
        self.game_activate = False

    def reset_stats(self) -> None:
        """
        初始化在游戏期间可能变化的统计信息
        :return:
        """
        self.ship_left = self.setting.ship_limit - 1
