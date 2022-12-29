import pyglet as pg


class Steve:
    def __init__(self, img='steve.png', x=0, y=0):
        pg.resource.path = [r'.\res']
        pg.resource.reindex()
        self.img = pg.resource.image(img)
        self.sprite = pg.sprite.Sprite(img=self.img)
        self.x = 0
        self.y = 0
        self.speed = 8
        self.ax = self.x * 32
        self.ay = self.y * 32
        self.sprite.y = self.ay
        self.sprite.x = self.ax

    def setx(self, x):
        self.x += x
        self.update_pos()

    def sety(self, y):
        self.y += y
        self.update_pos()

    def update_pos(self):
        self.ax = self.x * 32
        self.ay = self.y * 32
        self.sprite.y = self.ay
        self.sprite.x = self.ax

    def draw(self):
        self.sprite.draw()

    def rmove(self, dt=1/120):
        if self.sprite.x < 768-15:
            self.sprite.x += self.speed

    def lmove(self, dt=1/120):
        if self.sprite.x > 0:
            self.sprite.x -= self.speed

