#!/usr/bin/env python3

import numpy as np
from matplotlib import pyplot as plt
from Transformations_2D.Point2D import Point2D
from Transformations_2D.Rotate import Rotate
from Transformations_2D.Translate import Translate
from Transformations_2D.Transformation import Transformation


def test1():
    # Set up the points
    points = [Point2D(2, 4), Point2D(3, 6), Point2D(), Point2D(1, 2)]
    for p in points:
        print(p)

    # Set up the transformations
    t1 = Translate(1, 0)
    r1 = Rotate(np.pi/8)
    T1 = Transformation(t1, r1)
    print(t1, r1, T1)

    # Do operations with points
    points.sort()
    p_total = Point2D()
    for p in points:
        p_total = p_total + p
        print(p)
    print(p_total)

    # Do operations with transformations
    print(t1+t1)
    print(r1+r1)
    for p in points:
        p.plot('r')   # color red
        p_t = t1 * p
        p_t.plot('b') # color blue
        p_r = r1 * p
        p_r.plot('g') # color green
        p_T = T1 * p
        p_T.plot('y') # color yellow

    plt.axis('equal')

def run_tests():
    test1()

if __name__ == "__main__":
    run_tests()
