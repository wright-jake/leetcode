#example input
nums = [-2,1,-3,4,-1,2,1,-5,4]

#solution
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #start with first number in list
        current_sub = max_sub = nums[0]
        
        #continue with number after first number
        for num in nums[1:]:
            
            #which is bigger our current number or the previous sub plus the current number?
            current_sub = max(num, current_sub + num)
            
            #which is bigger our maximum sub or the current sub?
            max_sub = max(max_sub, current_sub)
        
        #return the maximum sub
        return max_sub
