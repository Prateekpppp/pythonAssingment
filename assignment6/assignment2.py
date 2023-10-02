class Dog:
    def __init__(self,name,age,coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(self.name)
        print(self.age)

    def get_info(self):
        print(self.coat_color)


class JackRussellTerrier(Dog):
    def function1(self):
        # print('function1')
        self.description()

    def function2(self):
        # print('function2')
        self.get_info()


class Bulldog(Dog):
    def function1():
        print('function1')

    def function2():
        print('function2')


obj1 = JackRussellTerrier('tom',15,'black')
obj1.function1()
obj1.function2()

obj2 = Bulldog('tom2',20,'black2')
obj2.description()
obj2.get_info()





    
