import pyglet as pg


blocks = []

class Block:
    def __init__(self, x, y, name, win: pg.window.Window, batch):
        global blocks
        blocks.append(self)
        self.x = x * 32
        self.y = y * 32
        self.name = name
        self.win = win
        pg.resource.path = [r'.\res']
        pg.resource.reindex()
        self.img = pg.resource.image(fr"{name}.png")
        self.sprite = pg.sprite.Sprite(img=self.img, batch=batch)
        self.sprite.x = self.x
        self.sprite.y = self.y

    def draw(self):
        self.sprite.x = self.x
        self.sprite.y = self.y
        self.sprite.draw()

    def __bool__(self):
        return True
