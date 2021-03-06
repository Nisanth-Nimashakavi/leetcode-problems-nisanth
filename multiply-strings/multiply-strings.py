class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        result = 0
        resul = 0
        value = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        for digit in num1:
            result = 10 * result + value[digit]
        for digit in num2:
            resul = 10 * resul + value[digit]
        num3 = result*resul
        x = "%s" % num3
        return x
    