import pyglet as pg
from random import random, randint
from block import Block, blocks


class XyCraft:
    def __init__(self):
        self.win = pg.window.Window(
            width=768,
            height=512
        )

        # 加载资源
        pg.resource.path = [r'.\res']
        pg.resource.reindex()
        self.sky = pg.resource.image(r"sky.png")

        # 地形生成

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

        # 地下基层岩石生成
        for y in range(6):
            for x in range(24):
                self.world_blocks[y][x] = Block(x, y, 'stone', self.win)

        # 地表地形生成
        # 生成草块
        for y in range(6, 14):
            for x in range(24):
                is_grass_probability = y / 25  # 是草块的概率随着高度增加而增加
                if (isinstance(
                        self.world_blocks[y - 1][x], type(0))):  # 如果它的下面是空气
                    is_grass_probability = 0  # 概率为0
                elif (self.world_blocks[y - 1][x].name == 'grass'):  # 如果它的下面是草块
                    is_grass_probability = 1 / 15  # 则概率固定在1/15
                if (random() < is_grass_probability):
                    self.world_blocks[y][x] = Block(x, y, 'grass', self.win)

                else:
                    is_grass_probability = 1  # 是除特殊情况，永远是石头：
                    if (isinstance(
                            self.world_blocks[y - 1][x], type(0))):  # 如果它的下面是空气
                        is_grass_probability = 0  # 概率为0
                    elif (self.world_blocks[y - 1][x].name == 'grass'):  # 如果它的下面是草块
                        is_grass_probability = 0  # 概率为0
                    if (random() < is_grass_probability):

                        self.world_blocks[y][x] = Block(x, y, 'stone', self.win)

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
