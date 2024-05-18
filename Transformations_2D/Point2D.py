from matplotlib import pyplot as plt

class Point2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Point2D(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Point2D({self.x}, {self.y})"

    def plot(self, color='r'):
        plt.plot(self.x, self.y, marker='o', color=color)
    
    def __lt__(self, other):
        return self.x < other.x
