import math
from app import *
from integration import *


class IntegrationApp(PyApp):
    def __init__(self):
        W, H = 1000, 700
        super().__init__('Integration', Size(W, H), 60)
        self.xy = XY(Point(100, H - 100), Vector(150, 150))

    def on_start(self):
        pass

    def on_event(self, event: Event):
        if event.type == Event.Type.QUIT:
            self.stop()


    def on_control(self, mouse: Mouse, keyboard: Keyboard):
        pass

    def on_update(self):
        pass

    def on_draw(self, surface: Surface):
        surface.fill(Color(230, 230, 80))
        draw = surface.draw()
        draw.line(
            self.xy.original(Point(-1000, 0)),
            self.xy.original(Point(1000, 0)),
            width = 2
        )
        draw.line(
            self.xy.original(Point(0, 1000)),
            self.xy.original(Point(0, -1000)),
            width = 2
        )
        x = -10
        while x <= 10:
            y = math.exp(-2 * x)
            p = Point(x, y)
            draw.circle(Circle(self.xy.original(p), 1))
            x += 0.001

    def on_stop(self):
        pass

if __name__ == '__main__':
    print(RecursiveIntegral(lambda x: x ** 2, Interval(-1, 1)).value())

    app = IntegrationApp()
    app.run()
