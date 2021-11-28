#example input
nums = [-1,0,3,5,9,12], target = 9

#solution
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #left and right pointers 
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            
            #find midpoint of list
            midpoint = left + (right - left) // 2
            
            #if midpoint is equal to target return the index of this (midpoint)
            if nums[midpoint] == target:
                return midpoint
            
            #if target is less than midpoint then our target must be to the left of the midpoint
            if target < nums[midpoint]:
                
                #change right pointer to left side of midpoint
                right = midpoint - 1
            
            #if not then the target must be to the right of the midpoint
            else:
                
                #change left pointer to right side of midpoint
                left = midpoint + 1
        
        #if target does not exist then returns -1
        return -1
