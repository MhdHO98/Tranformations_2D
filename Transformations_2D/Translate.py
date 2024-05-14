class Translate:
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy
    
    def __call__(self, point):
        return Point2D(point.x + self.dx, point.y + self.dy)
    
    def __mul__(self, other):
        if isinstance(other, Point2D):
            return self.__call__(other)
    
    def __repr__(self):
        return f"Translate(dx={self.dx}, dy={self.dy})"
    
    def __add__(self, other):
        if isinstance(other, Translate):
            return Translate(self.dx + other.dx, self.dy + other.dy)
