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


obj = Student()

obj.getName()
obj.getRollNumber()