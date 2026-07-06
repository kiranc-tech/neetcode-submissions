class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        size=len(nums)-1
        for j in range(size):
            for i in range(0,size):
                if nums[i]>nums[i+1]:
                   nums[i],nums[i+1]=nums[i+1],nums[i]

                
        return nums