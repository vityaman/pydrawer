from collections import deque
from app.graphics.figure.value import Size, Color, Point, Vector
from app.graphics.figure.value.transformation import rotation
from app.graphics.figure import Circle, Rectangle
from app.graphics import Surface, Transformed
from app.control import Event
from app import PyApp


class HelloWorld(PyApp):
    def __init__(self):
        self.W = 500
        self.H = 500
        super().__init__(
            title='Hello World',
            window_size=Size(self.W, self.H),
            fps=60
        )
        self.colors = [
            Color(255, 0, 0),
            Color(50, 200, 50),
            Color(0, 0, 255),
        ]
        self.arrows = [
            Vector(4, 0), 
            Vector(3, 0),
            Vector(2, 0)
        ]
        self.rotations = [
            rotation(-0.2),
            rotation(0.05),
            rotation(0.3)
        ]
        self.points = [
            deque([Point(0, 0), Point(0, 0)]),
            deque([Point(0, 0), Point(0, 0)]),
            deque([Point(0, 0), Point(0, 0)])
        ]

    def on_event(self, event: Event):
        if event.type == Event.Type.QUIT:
            self.stop()

    def on_update(self):
        for i in range(len(self.points)):
            self.arrows[i] = self.rotations[i].apply(self.arrows[i])
            self.points[i].appendleft(self.arrows[i])
            if (len(self.points[i]) > 10):
                self.points[i].pop()

    def on_draw(self, surface: Surface):
        surface.fill(Color(230, 230, 80))
        draw = Transformed.scaled(
            Transformed.xoy(
                origin = surface.draw(),
                center = Point(
                    x = self.W / 2,
                    y = self.H / 2
                )
            ).text(
                position = Point(0, 0),
                text = 'Hello World'
            ).text(
                position = Point(0, -10),
                text = 'Pydrawer'
            ).circle(
                circle = Circle(
                    center = Point(0, 0),
                    radius = 40
                ),
                width = 1
            ),
            scale = Vector(40, 40)
        ).line(
            start = Point(-10, 0),
            end = Point(10, 0)
        ).line(
            start = Point(0, -10),
            end = Point(0, 10)
        ).lines(
            points = (
                Point(x, x ** 2) for x in map(
                    lambda x: x / 1000, (n for n in range(-1000, 3000))
                )
            )
        ).text(
            position = Point(2, 2),
            text = "y = x ^ 2, x in [-1, 3]"
        ).rect(
            rectangle = Rectangle(-2, 2, -2, 2),
            width = 1
        )
        for i in range(len(self.arrows)):
            draw.color(
                    self.colors[i]
                ).line(
                    start = Vector(0, 0),
                    end = self.arrows[i],
                    width = 2
                ).lines(
                    points = self.points[i],
                    width = 2
                )


if __name__ == '__main__':
    app = HelloWorld()
    app.run()
