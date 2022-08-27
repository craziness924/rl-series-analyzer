class Point():
    def __init__(self, x: float, y: float, color: str = "magenta", marker: str = "."):
        self.x = x
        self.y = y
        self.color = color
        self.marker = marker

    def __str__(self):
        return f"{self.x} {self.y} {self.color} {self.marker}"