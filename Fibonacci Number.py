#example input
n=3

#solution
class Solution:
    def fib(self, n: int) -> int:
        #create a dictionary to store the known fibonacci numbers
        num = {0: 0, 1: 1}
        
        #we now want to add the remaining fibonacci numbers, from 2 to n + 1 (as we will want to look at n itself)
        for i in range(2, n+1):
            
            #the formula
            num[i] = num[i-1] + num[i-2]
        
        #return the fibonacci number
        return(num[n])
