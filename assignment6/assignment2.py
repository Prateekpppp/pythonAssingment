class Dog:
    def __init__(self,name,age,coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color
​
    def description(self):
        print(self.name)
        print(self.age)
​
    def get_info(self):
        print(self.coat_color)
​
​
class JackRussellTerrier(Dog):
    def function1():
        print('function1')
​
    def function2():
        print('function2')
​
​
class Bulldog(Dog):
    def function1():
        print('function1')
​
    def function2():
        print('function2')
​
​
obj1 = JackRussellTerrier('tom',10045,'black')
obj1.description()
obj1.get_info()
​
obj2 = Bulldog('tom2',10045,'black2')
obj2.description()
obj2.get_info()
​
​
​
​
​
    
