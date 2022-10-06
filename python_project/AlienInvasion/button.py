import pygame.font


class Button(object):
    def __init__(self, ai_game, msg: str = "Play") -> None:
        """
        初始化按钮属性
        """
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        # 设置按钮的大小和其它属性
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        # 创建按钮rect对象，并且使其居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        # 按钮事件标签只需要创建一次
        self._prep_msg(msg)

    def _prep_msg(self, msg: str = "Play") -> None:
        """
        将msg渲染成图像，并且使其在按钮上居中
        :param msg:
        :return:
        """
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self) -> None:
        """
        绘制一个颜色填充按钮，并且绘制文本
        :return:
        """
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)