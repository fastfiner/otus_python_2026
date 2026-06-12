from src import Rectangle, Square, Circle, Triangle

r = Rectangle(3, 5)
s = Square(5)
c = Circle(10)
t = Triangle(4, 3, 5)

print(r.add_area(s))
print(r.add_area(c))
print(r.add_area(t))
print(s.add_area(c))
print(s.add_area(t))
print(c.add_area(t))
