import pyglet as pg


blocks = []

class Block:
    def __init__(self, x, y, name, win: pg.window.Window):
        global blocks
        blocks.append(self)
        self.x = x * 32
        self.y = y * 32
        self.win = win
        pg.resource.path = [r'.\res']
        pg.resource.reindex()
        self.img = pg.resource.image(fr"{name}.png")


    def draw(self):
        self.img.blit(self.x, self.y)
