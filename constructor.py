# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def move(self):
#         print('move')
    
#     def draw(self):
#         print("draw")
# point = Point(10, 20)
# print(point.x)

class Person:
    def __init__(self, name) -> None:
        self.name = name
    
    def talk(self):
        print(f'{self.name} is talking!')

person1 = Person('James')
person2 = Person('Christine')
person1.talk()
person2.talk()