#example input
x = 121

#solution
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return(str(x)==str(x)[::-1])
