import time
import pyglet as pg


class Steve:
    def __init__(self, xc_game, x=0, y=0):
        pg.resource.path = [r'.\res']
        pg.resource.reindex()
        self.rimg = pg.resource.image('steve-right.png')
        self.limg = pg.resource.image('steve-left.png')
        self.sprite = pg.sprite.Sprite(img=self.rimg)
        self.x = 0  # 坐标的x
        self.y = 0  # 坐标的y
        self.speed = 10
        self.ax = self.x * 32  # 在世界中方块位置的x
        self.ay = self.y * 32  # 在世界中按方块位置的y
        self.x = 0
        self.y = 0
        self.speed = 10
        self.ax = self.x * 32
        self.ay = self.y * 32
        self.sprite.y = self.ay
        self.sprite.x = self.ax
        self.xc_game = xc_game
        self.init_steve()

    def setx(self, x):
        self.x = x
        self.update_pos()

    def sety(self, y):
        self.y = y
        self.update_pos()

    def update_pos(self):
        self.ax = self.x * 32
        self.ay = self.y * 32
        self.sprite.y = self.ay
        self.sprite.x = self.ax

    def draw(self):
        self.sprite.draw()

    def rmove(self):
        if self.sprite.x < 768-15:
            self.sprite.x += self.speed
            self.sprite.image = self.rimg

    def lmove(self):
        if self.sprite.x > 0:
            self.sprite.x -= self.speed
            self.sprite.image = self.limg

    def fall(self, y=1):
        for i in range(y):
            for j in range(16):
                self.sprite.y -= 2

    def jump(self, y=1):
        for i in range(y):
            for j in range(16):
                self.sprite.y += 2

    def init_steve(self):
        for y in range(15, -1, -1):
            if self.xc_game.is_air(0, y):
                continue
            else:
                self.y = y + 1
                break
        self.update_pos()
