class MathDojo():
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        self.result += num
        for i in nums:
            self.result += i
        return self
    def subtract(self, num, *nums):
        self.result -= num
        for i in nums:
            self.result -= i
        return self

md = MathDojo()

x = md.add(2).add(2,5,1).subtract(2,3).result
print(x)
x = md.add(5,3,6,7,3).add(1).add(589,34,98).result
print(x)
x = md.subtract(58).subtract(1,2,3,4,5,6,6,7,8,89).subtract(409).result
print(x)