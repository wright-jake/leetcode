#example input
nums = [2,7,11,15], target = 9

#solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sum = nums[i]+nums[j]
                if sum == target:
                    return[i,j]
