#!/usr/bin/env python

import Shape

a = Shape.Point()
repr(a)
b = Shape.Point(3, 4)
str(b)
b.distance_from_origin()
b.x = -19
str(b)
a == b, a != b

p = Shape.Point(28, 45)
c = Shape.Circle(5, 28, 45)
p.distance_from_origin()
c.distance_from_origin()
