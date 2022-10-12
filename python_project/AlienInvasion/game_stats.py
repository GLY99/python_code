import os
import json


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
        self.score = 0
        self.level = 1
        self.reset_stats()
        self.game_activate = False
        self.high_score = self.read_high_score_from_file()

    def reset_stats(self) -> None:
        """
        初始化在游戏期间可能变化的统计信息
        :return:
        """
        self.ship_left = self.setting.ship_limit - 1
        self.score = 0
        self.level = 1

    def write_high_score_to_file(self) -> None:
        """
        将最高分写入文件
        :return:
        """
        filename = "high_score.txt"
        if not os.path.exists(filename):
            with open(filename, 'w') as f:
                json.dump(self.high_score, f)
        else:
            with open(filename, 'r+') as f:
                try:
                    file_high_score = json.load(f)
                except json.decoder.JSONDecodeError:
                    f.seek(0)
                    f.truncate()
                    json.dump(self.high_score, f)
                else:
                    if file_high_score < self.high_score:
                        f.seek(0)
                        f.truncate()
                        json.dump(self.high_score, f)

    @staticmethod
    def read_high_score_from_file() -> int:
        """
        从文件中读取到最高分
        :return:
        """
        filename = "high_score.txt"
        high_score = 0
        if not os.path.exists(filename):
            return high_score
        else:
            with open(filename) as f:
                try:
                    high_score = json.load(f)
                except json.decoder.JSONDecodeError:
                    return 0
                else:
                    return high_score


