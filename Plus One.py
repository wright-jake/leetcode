#example input
digits = [1,2,3]

#solution
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        #iterate through the array
        for i in range(n):
            
            #iterate through the array from the end
            idx = n - 1 - i
            
            #set all the nines at the end of array to zeros
            if digits[idx] == 9:
                digits[idx] = 0
            
            #the rightmost not-nine
            else:
                
                # increase this rightmost not-nine by 1
                digits[idx] += 1
                return digits

        #if all digits are nines then we need to add a 1 to the front
        return [1] + digits
