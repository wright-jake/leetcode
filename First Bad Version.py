#example input
n = 5, bad = 4

#solution
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        
        while left < right:
            
            midpoint = (left + right) // 2
            
            if isBadVersion(midpoint):
                right = midpoint
            else:
                
                #if midpoint isn't bad then all the numbers to the left will also be good, therefore we need to shift the midpoint to the right by 1
                left = midpoint + 1
        
        return left
