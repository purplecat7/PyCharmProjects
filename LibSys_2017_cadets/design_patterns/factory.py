# coding=utf-8
# Factory/shapefact1/ShapeFactory1.py
# A simple static factory method.
# http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Factory.html
from __future__ import generators
import random

class Shape(object):
    # Create based on class name:
    def factory(type):
        #return eval(type + "()")
        if type == "Circle": return Circle()
        if type == "Square": return Square()
        if type == "Triangle": return Triangle()
        assert 0, "Bad shape creation: " + type
    factory = staticmethod(factory)

class Circle(Shape):
    def draw(self): print("Circle.draw")
    def erase(self): print("Circle.erase")

class Square(Shape):
    def draw(self): print("Square.draw")
    def erase(self): print("Square.erase")

class Triangle(Shape):
    def draw(self): print ("Triangle.draw")
    def erase(self): print ("Triangle.erase")

# Generate shape name strings:
# the 'yield' keyword determines that this function is a generator and it
# actually returns a generator object that has an iterator.
# This iterator is implicitly used in the for statement, so it appears that
# you are iterating through the generator function, not what it returns.
# This was done for convenience of use.

# Thus, the code that you write is actually a kind of factory,
# that creates the generator objects that do the actual generation.
# You can use the generator explicitly if you want, for example:
#   gen = shapeNameGen(7)
#   print(gen.next())

# So next() is the iterator method that’s actually called to generate the
# next object, and it takes no arguments. shapeNameGen( ) is the factory,
# and gen is the generator.
def shapeNameGen(n):
    types = Shape.__subclasses__()
    for i in range(n):
        yield random.choice(types).__name__

# generators are a bit odd! the shapeNameGen(7) is not an initialisation
shapes = [ Shape.factory(i) for i in shapeNameGen(9)]

for shape in shapes:
    shape.draw()
    shape.erase()