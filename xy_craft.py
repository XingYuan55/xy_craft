import pyglet as pg
from random import random, randint
from block import Block, blocks


class XyCraft:
    def __init__(self):
        self.win = pg.window.Window(
            width=768,
            height=512
        )

        self.world_blocks = [  # 方块列表
            [_ for _ in range(24)],  # y=0
            [_ for _ in range(24)],  # y=1
            [_ for _ in range(24)],  # y=2
            [_ for _ in range(24)],  # y=3
            [_ for _ in range(24)],  # y=4
            [_ for _ in range(24)],  # y=5
            [_ for _ in range(24)],  # y=6
            [_ for _ in range(24)],  # y=7
            [_ for _ in range(24)],  # y=8
            [_ for _ in range(24)],  # y=9
            [_ for _ in range(24)],  # y=10
            [_ for _ in range(24)],  # y=11
            [_ for _ in range(24)],  # y=12
            [_ for _ in range(24)],  # y=13
            [_ for _ in range(24)],  # y=14
            [_ for _ in range(24)],  # y=15
        ]  # 这些奇怪的循环是占位符

        # 加载资源
        pg.resource.path = [r'.\res']
        pg.resource.reindex()
        self.sky = pg.resource.image(r"sky.png")

        self.create_world()

        @self.win.event
        def on_draw():
            self.win.clear()
            self.sky.blit(0, 0)
            for block in blocks:
                block.draw()

        @self.win.event
        def on_key_press(symbol, modifiers):
            self.on_key_press(symbol, modifiers)

        @self.win.event
        def on_text(text):
            self.on_text(text)

    def create_world(self):
        # 地形生成

        # 地下基层岩石生成
        for y in range(6):
            for x in range(24):
                self.world_blocks[y][x] = Block(x, y, 'stone', self.win)

        # 地表地形生成
        for y in range(6, 14):
            for x in range(24):
                if not self.create_grass(x, y):
                    self.create_stone(x, y)

    def create_grass(self, x, y):
        # 生成草块
        is_grass_probability = y / 25  # 是草块的概率随着高度增加而增加
        try:
            if self.is_air(x + 1, y):
                is_grass_probability += 1 / 15
            if self.is_air(x + 1, y):
                is_grass_probability += 1 / 15
                if self.is_air(x + 1, y):
                    is_grass_probability += 1 / 15
        except IndexError:
            ...

        if (isinstance(
                self.world_blocks[y - 1][x], type(0))):  # 如果它的下面是空气
            is_grass_probability = 0  # 概率为0
        elif (self.world_blocks[y - 1][x].name == 'grass'):  # 如果它的下面是草块
            is_grass_probability /= 10  # 则概率除以10

        if random() < is_grass_probability:
            self.world_blocks[y][x] = Block(x, y, 'grass', self.win)
            return True
        else:
            return False

    def create_stone(self, x, y):
        is_grass_probability = 10 / y  # 是除特殊情况，永远是石头：
        if (isinstance(
                self.world_blocks[y - 1][x], type(0))):  # 如果它的下面是空气
            is_grass_probability = 0  # 概率为0
        elif (self.world_blocks[y - 1][x].name == 'grass'):  # 如果它的下面是草块
            is_grass_probability = 0  # 概率为0
        if (random() < is_grass_probability):
            self.world_blocks[y][x] = Block(
                x, y, 'stone', self.win)

    def is_air(self, x, y):
        return isinstance(self.world_blocks[y][x], type(0))

    def on_draw(self):
        self.win.clear()
        self.stone.blit(0, 0)
        self.grass.blit(0, 32)

    def on_key_press(self, symbol, modifiers):
        print(symbol)

    def on_text(self, text):
        print(text)


craft = XyCraft()
pg.app.run()
