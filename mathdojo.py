class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        self.result += num
        for i in range(0, len(nums)):
            self.result += nums[i]
        # print(self.result)
        return self  
    def subtract(self, num, *nums):
        self.result -= num
        for i in range(0, len(nums)):
            self.result -= nums[i]
        # print(self.result)
        return self
# create an instance:
md = MathDojo()
# to test:
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)	# should print 5
# run each of the methods a few more times and check the result!
testadd = md.add(3).add(1,3,5).add(1,2,3,4,5,6).result
print(testadd)
testsubtract = md.subtract(30).subtract(1,3,5).subtract(1,2,3,4,5,6).result
print(testsubtract)