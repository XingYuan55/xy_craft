import pyglet as pg
from random import random
from block import Block
from steve import Steve


class XyCraft:
    def __init__(self):
        self.win = pg.window.Window(
            width=768,
            height=512,
        )

        self.world_blocks = [  # 方块列表
<<<<<<< HEAD
            [_ for _ in range(24)],  #  y=0
=======
            [_ for _ in range(24)],  # y=0
>>>>>>> 372e3d326d90b341a3f1027075b0349ed5ef71b5
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
<<<<<<< HEAD
        ]  # 这些奇怪的循环是占位
=======
        ]  # 这些奇怪的循环是占位符
>>>>>>> 372e3d326d90b341a3f1027075b0349ed5ef71b5
        self.blocks_batch = pg.graphics.Batch()
        # 加载资源
        pg.resource.path = [r'.\res']
        pg.resource.reindex()
        self.sky = pg.resource.image(r"sky.png")
        self.create_world()
        self.steve = Steve(self)
<<<<<<< HEAD
=======


>>>>>>> 372e3d326d90b341a3f1027075b0349ed5ef71b5
        @self.win.event
        def on_draw():
            self.win.clear()
            self.sky.blit(0, 0)
            # for block in blocks:
            #     block.draw()
            self.blocks_batch.draw()
            self.steve.draw()

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
                # noinspection PyTypeChecker
                self.world_blocks[y][x] = Block(
                    x, y, 'stone', self.win, self.blocks_batch)

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
                is_grass_probability += 1 / 20
            if self.is_air(x - 1, y):
                is_grass_probability += 1 / 20
            if self.is_air(x, y + 1):
                is_grass_probability += 1 / 20
        except IndexError:
            ...

        if (isinstance(
                self.world_blocks[y - 1][x], type(0))):  # 如果它的下面是空气
            is_grass_probability = 0  # 概率为0
        elif (self.world_blocks[y - 1][x].name == 'grass'):  # 如果它的下面是草块
            is_grass_probability /= 10  # 则概率除以10

        if random() < is_grass_probability:
            # noinspection PyTypeChecker
            self.world_blocks[y][x] = Block(
                x, y, 'grass', self.win, self.blocks_batch)
            return True
        else:
            return False

    def create_stone(self, x, y):
        is_grass_probability = 10 / y  # 是除特殊情况，永远是石头：
        if (isinstance(
                self.world_blocks[y - 1][x], type(0))):  # 如果它的下面是空气
            is_grass_probability = 0  # 概率为0
        elif self.world_blocks[y - 1][x].name == 'grass':  # 如果它的下面是草块
            is_grass_probability = 0  # 概率为0
        if random() < is_grass_probability:
            # noinspection PyTypeChecker
            self.world_blocks[y][x] = Block(
                x, y, 'stone', self.win, self.blocks_batch)

<<<<<<< HEAD
    def steve_can_move(self, direction_x, direction_y):
        if (self.is_air(self.steve.ax + direction_x, self.steve.ay)) or (self.is_air(self.steve.ax + direction_x, self.steve.ay + 1)):
            return True
        else:
            return False

=======
>>>>>>> 372e3d326d90b341a3f1027075b0349ed5ef71b5
    def is_air(self, x, y):
        return type(self.world_blocks[y][x]) == type(0)

    def on_key_press(self, symbol, modifiers):
<<<<<<< HEAD
        # print(symbol)
        # if symbol == pg.window.key.A:
        #     self.steve.lmove()
        # if symbol == pg.window.key.D:
        #     self.steve.rmove()
        ...

    def on_text(self, text):
        print(self.steve.ax)
        if text == 'a':
            if self.steve_can_move(1, 0):
                self.steve.lmove()
        if text == 'd':
            if self.steve_can_move(-1, 0):
                self.steve.rmove()
        ...
=======
        ...

    def on_text(self, text):
        if text == 'a':
            self.steve.lmove()
        if text == 'd':
            self.steve.rmove()

>>>>>>> 372e3d326d90b341a3f1027075b0349ed5ef71b5

craft = XyCraft()
pg.app.run()
