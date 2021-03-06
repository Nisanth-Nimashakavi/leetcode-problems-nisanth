class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        x = 0
        output = []
        for i in range(len(nums)):
            x = x + nums[i]
            print(x)
            output.append(x)

        print(output)
        return output