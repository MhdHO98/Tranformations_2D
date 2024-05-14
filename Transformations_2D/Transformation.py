class Transformation:
    def __init__(self, *transforms):
        self.transforms = transforms
    
    def __call__(self, point):
        for transform in self.transforms:
            point = transform(point)
        return point

    def __mul__(self, other):
        if isinstance(other, Point2D):
            return self.__call__(other)

    def __repr__(self):
        return f"Transformation({', '.join(str(t) for t in self.transforms)})"
