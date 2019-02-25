import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """子弹发射管理类"""
    def __init__(self,ai_settings,screen,ship):
        """创建子弹对象"""
        super(Bullet,self).__init__()
        self.screen=screen

        #初始化子弹位置
        self.rect=pygame.Rect(0,0,ai_settings.bullet_width,
                              ai_settings.bullet_height)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top
        #存储小数
        self.y=float(self.rect.y)

        self.color=ai_settings.bullet_color
        self.speed_factor=ai_settings.bullet_speed_factor
        
    def update(self):
        """向上移动子弹"""
        #跟新子弹位置（小数值）
        self.y -=self.speed_factor
        #跟新子弹位置（rect）
        self.rect.y=self.y

    def draw_bullet(self):
        """绘制子弹"""
        pygame.draw.rect(self.screen,self.color,self.rect)
    
