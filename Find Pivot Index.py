#example input
nums = [2,1,-1]

#solution
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)
        
        #we want to iterate through the entire array
        for i in range(len(nums)):
            
            #decrease the right sum by the value we increase the left sum by
            right_sum -= nums[i]
            
            if left_sum == right_sum:
                
                #return pivot if left and right sum are equal
                return i
            
            else:
                left_sum += nums[i]
        
        #if no index exists return -1
        return -1
