class Screen:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def render(self, sprite, x, y):
        print(f"rendering a {sprite.type} sprite at x:{x}, y:{y}")