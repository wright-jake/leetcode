#example input
nums = [1, 2, 3, 4, 5]

#solution
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        
        #if there is only one number in the list then we cannot compare maximum's
        if len(nums) == 1: 
            return 0
        
        #create a second list with the same numbers
        nums_2 = list(nums)
        
        #largest element in nums
        first = max(nums_2)
        
        #remove the largest element 
        nums_2.remove(first)
        
        #now we can find the second largest element in nums
        second = max(nums_2)

        #if original largest element is greater than or equal to 2 * second largest element then we can return the index
        if first >= second * 2: 
            return nums.index(first)
        
        #if not then we return 1
        else:
            return -1
