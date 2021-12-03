#example input
n = 3

#solution
lass Solution:
    def tribonacci(self, n: int) -> int:
        #create a dictionary to store the known tribonacci numbers
        num = {0: 0, 1: 1, 2: 1}
        
        #we now want to add the remaining tribonacci numbers, from 0 to n + 1 (as we will want to look at n itself)
        for i in range(0, n+1):
            
            #the formula
            num[i+3] = num[i] + num[i+1] + num[i+2]
        
        #return the tribonacci number
        return(num[n])
