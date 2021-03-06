class Solution:
    def findNthDigit(self, n: int) -> int:
        x = 9
        y = 1
        while n > x*y:
            n -= (x*y)
            x = x* 10
            y = y + 1
        
        x = int(10**(y-1) + (n/y));
        n =n % y
        if n == 0: return (x-1)%10
        return int(str(x)[n-1])