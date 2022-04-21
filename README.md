# PyDrawer


## The simplest gui
Created to simplify the creation of gui applications using python.
The simplest functionality is provided for fast lightweigth apps.
It can be usefull if you want to quick throw some idea of yours on the draft.


## Requirements
- ```pip install pygame```


## Example

```python
from app import *


class HelloWorld(PyApp):
    def __init__(self):
        super().__init__(
            title='Hello World',
            window_size=Size(
                width=500,
                height=500
            ),
            fps=60
        )

    def on_event(self, event: Event):
        if event.type == Event.Type.QUIT:
            self.stop()

    def on_draw(self, surface: Surface):
        surface.fill(Color(230, 230, 80))
        surface.draw()\
            .text(position = Point(250, 250),
                  text = 'Hello World')\
            .circle(circle = Circle(center = Point(250, 250),
                                    radius = 40))

if __name__ == '__main__':
    app = HelloWorld()
    app.run()
```