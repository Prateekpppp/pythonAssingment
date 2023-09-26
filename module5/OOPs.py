# Challenge1

class SquareNum :
    def __init__(self,x,y,z):
        self.x = x 
        self.y = y 
        self.z = z

    def sqSum(self) :
        sum = self.x**2 + self.y**2 + self.z**2
        print(sum)

# sm = SquareNum(1,2,3)

# sm.sqSum()


# Challenge2

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


# obj = Calculator(10, 94)
# obj.add()
# obj.subtract()
# obj.multiply()
# obj.divide()



# Challenge3

class Student :

    def __init__(self) :
        self.setName('test1')
        self.setRollNumber(94)

    def getName(self) :
        print(self._name)
        
    def setName(self, value) :
        self._name = value
        
    def getRollNumber(self) :
        print(self._rollNumber)
        
    def setRollNumber(self, value) :
        self._rollNumber = value


# obj = Student()

# obj.getName()
# obj.getRollNumber()


# Challenge4 and 5

class Account :

    def __init__(self, title=None, balance=0) :
        self.title = title
        self.balance = balance

    def getBalance(self):
        return self.balance
    
    def deposit(self,amount):
        self.balance += amount
        
    def withdrawal(self,amount):
        self.balance -= amount
        
    
class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title,balance)
        self.interestRate = interestRate

        print(title)
        print(balance)
        print(interestRate)

    def interestAmount(self):
        interest_amount = self.interestRate * self.balance/100
        
        return interest_amount

obj = SavingsAccount("Ashish", 5000, 5)

print(obj.interestAmount())

