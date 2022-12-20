import pyglet as pg


class Steve:
    def __init__(self, img='steve.png'):
        pg.resource.path = [r'.\res']
        pg.resource.reindex()
        self.img = pg.resource.image(img)
        self.sprite = pg.sprite.Sprite(img=self.img)

    def draw(self):
        self.sprite.draw()

    def rmove(self, dt=1/120):
        if self.sprite.x < 768-15:
            self.sprite.x += 15 * dt

    def lmove(self, dt=1/120):
        if self.sprite.x > 0:
            self.sprite.x += -15 * dt

