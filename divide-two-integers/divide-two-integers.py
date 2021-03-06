class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        import math 
        x = dividend / divisor
        print(x)
        if x >= (2**31)-1:
            return (2**31)-1
        elif x <= (-2**31):
            return (-2**31)
        else:
            if x > 0:
                return math.floor(x) 
            else: 
                return math.ceil(x)