import pyglet as pg


class XyCraft:
    def __init__(self):
        self.win = pg.window.Window(
            resizable=True,
        )

        @self.win.event
        def on_draw():
            self.win.clear()

        @self.win.event
        def on_key_press(symbol, modifiers):
            self.on_key_press(symbol, modifiers)

        @self.win.event
        def on_text(text):
            self.on_text(text)

    def on_draw(self):
        ...

    def on_key_press(self, symbol, modifiers):
        print(symbola)

    def on_text(self, text):
        print(text)

craft = XyCraft()
pg.app.run()