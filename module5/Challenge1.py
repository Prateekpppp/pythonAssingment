class SquareNum :
    def __init__(self,x,y,z):
        self.x = x 
        self.y = y 
        self.z = z

    def sqSum(self) :
        sum = self.x**2 + self.y**2 + self.z**2
        print(sum)

sm = SquareNum(1,2,3)

sm.sqSum()