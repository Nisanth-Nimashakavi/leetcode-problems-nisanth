class Solution:
    def sortColors(self, nums: List[int]) -> None:
        import copy
        """
        Do not return anything, modify nums in-place instead.
        """
        #nums.sort()
        new_list = copy.deepcopy(nums)
        num = []
        print(new_list)
        while new_list:
            minimum = new_list[0]
            for x in new_list: 
                if x < minimum:
                    minimum = x
            num.append(minimum)
            new_list.remove(minimum) 
        for index in range(len(num)):
            nums[index] = num[index] 
        print(num)
       #return nums
        