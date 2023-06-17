import math
class Nums:
    def __init__(self, num, num1):
        self.num = num
        self.num1 = num1

class Name(Nums):
    def error1(self):
        if self.num < 0:
            raise ValueError(f'You entered {self.num}')
        else:
            print(math.sqrt(self.num))

    def error2(self):
        if self.num == 0:
            raise ZeroDivisionError(f'You entered 0')
        else:
            print(self.num1/self.num)

    def error3(self):

        if self.num1 or self.num == str:
            raise TypeError("Unsupported operand type")
        else:
            print(self.num-self.num1)
    pass



var = Name(num=1, num1='1')

try:
    var.error1()
except ValueError as s:
    print(str(s))

try:
    var.error3()
except TypeError as s:
    print(str(s))

try:
    var.error2()
except ZeroDivisionError as e:
    print(str(e))