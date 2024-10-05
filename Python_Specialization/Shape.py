class Shape:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        return self.width * self.height

    def __add__(self, other):
        if isinstance(other, Shape):
            new_width = self.width + other.width
            new_height = self.height + other.height
            return Shape(new_width, new_height)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Shape):
            return self.area() > other.area()
        return NotImplemented


w1 = int(input())
h1 = int(input())
w2 = int(input())
h2 = int(input())

s1 = Shape(w1, h1)
s2 = Shape(w2, h2)
result = s1 + s2

print(result.area())
print(s1 > s2)