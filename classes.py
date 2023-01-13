

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")
    
    def draw(self):
        print("draw")

class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hi, I am {self.name}")





point1 = Point(10, 20)
print(point1.x)
point1.draw()
point1.move()


person1 = Person("glenn angus")
person1.talk()

person2 = Person("angus glenn")
person2.talk()
