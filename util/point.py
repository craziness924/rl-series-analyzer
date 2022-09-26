class Point():
    def __init__(self, x: float, y: float, color: str = "magenta", marker: str = "."):
        self.x = x
        self.y = y
        self.color = color
        self.marker = marker

    def __str__(self):
        return f"{self.x} {self.y} {self.color} {self.marker}"

class PiePoint():
    def __init__(self, x: float, color: str = "magenta", label: str = "", explode: float = 0.0):
        self.x: float = x
        self.color: str = color

        self.label: str = label
        self.explode: float = explode
    
    def __str__(self):
        return f"{self.x} {self.color} {self.label} {self.explode}"