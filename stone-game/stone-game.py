class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True
        y = 0 
        z = 0
        u = []
        x = len(piles)
        print(x)
        x = x/2
        while y !=x:
            y+=1
            z = piles(y) + z 
        print(z)
        