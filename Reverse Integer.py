#example input
x = 123

#solution
class Solution:
    def reverse(self, x: int) -> int:

        #initial reversed number
        sum=0
        
        #basic positive sign
        sign=1
        
        #if x is negative
        if x<0:
            sign=-1
            x=x*-1
        
        #loop to create the full reversed number
        while x>0:
            
            #we want to return the last digit using mod10
            rem=x%10
            
            #add this to our reversed number
            sum=sum*10+rem
            
            #use integer division to then loop back through
            x=x//10
        
        #if value goes outside 32-bit range return 0
        if not -2147483648<sum<2147483647:
            return 0
        
        #in case negative number at the start multiply to get back to negative
        return sign*sum
