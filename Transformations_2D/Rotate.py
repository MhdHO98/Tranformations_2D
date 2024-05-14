class Rotate:
    def __init__(self, theta):
        self.theta = theta
    
    def __call__(self, point):
        cos_theta, sin_theta = np.cos(self.theta), np.sin(self.theta)
        x_new = point.x * cos_theta - point.y * sin_theta
        y_new = point.x * sin_theta + point.y * cos_theta
        return Point2D(x_new, y_new)
    
    def __mul__(self, other):
        if isinstance(other, Point2D):
            return self.__call__(other)
    
    def __repr__(self):
        return f"Rotate(theta={self.theta})"
    
    def __add__(self, other):
        if isinstance(other, Rotate):
            return Rotate(self.theta + other.theta)
