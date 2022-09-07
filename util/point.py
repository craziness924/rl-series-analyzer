class Point():
    def __init__(self, x: float, y: float = None, color: str = "magenta", marker: str = ".", label: str = None, explode: float = None):
        self.x = x
        self.y = y
        self.color = color
        self.marker = marker
        self.label = label
        self.explode = explode


    def __str__(self):
        return f"{self.x} {self.y} {self.color} {self.marker} {self.label} {self.explode}"