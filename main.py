"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

# Questions
# 1. Exercise 1.1 #8. Symmetry. In general, types of symmetry:
#   - Rotational
#   - X
#   - Y
# 2. For a given angle, how many turns does it take before it cycles?

import turtle

t = turtle.Turtle()

def poly(side, angle):
  rotations = 0
  while True:
    polystep(side, angle)

    rotations += 1
    if t.heading() == 0:
      print(rotations, 'turns')
      return

def doublepoly(side1, side2, angle):
  rotations = 0
  while True:
    t.color('red')
    polystep(side1, angle/2)
    t.color('green')
    polystep(side2, angle/2)

    rotations += 1
    if t.heading() == 0:
      print(rotations, 'turns')
      return

def polystep(side, angle):
  t.forward(side)
  t.right(angle)

print(75*24)
ang = 16
import math
print(math.gcd(75,360))
t.speed("fastest")
poly(14, ang)
#doublepoly(100, 40, ang)
