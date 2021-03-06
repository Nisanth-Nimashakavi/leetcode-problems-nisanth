class Solution:
    def reverse(self, x: int) -> int:
        # convert to string, reverse, convert to int?
        x = str(x)
        x = x[::-1]
        if '-' in x:
            x = x.strip('-')
            x = -1*int(x)
        else:
            x = int(x)
        if x >= (-2)**31 and x <= (2**31) - 1:
            return x
        else:
            return 0