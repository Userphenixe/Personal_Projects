import matplotlib.pyplot as plt
class circle (object):
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
    def add_radius(self, value):
        self.radius = self.radius + value
        return self.radius
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()
class rectangle (object):
    def __init__(self, height, width, color):
        self.height = height
        self.width = width
        self.color = color
x = circle(3.14, 'yellow')
y = rectangle(6, 3, 'red')
print(type(x))
print(type(y))
print(x.radius, x.color)
try :
    x = circle(radius=2.2, color='green')
    print(x.radius, x.color)
except:
    print("something went wrong")
finally:
    print("continuing the process")
print(y.height, y.width, y.color)
x.add_radius(2.1)
print(x.radius)
x.drawCircle()