class Calculator :
    def __init__(self,num1,num2):
        self.num1 = num1 
        self.num2 = num2

    def add(self) :
        sum = self.num1 + self.num2
        print(sum)

    def subtract(self) :
        if self.num1 > self.num2 :
            subtract = self.num1 - self.num2
        else :
            subtract = self.num2 - self.num1

        print(subtract)

    def multiply(self) :
        multiple = self.num1 * self.num2
        print(multiple)
    
    def divide(self) :
        div = self.num2/self.num1
        print(div)


obj = Calculator(10, 94)
obj.add()
obj.subtract()
obj.multiply()
obj.divide()