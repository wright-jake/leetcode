#example input
numRows = 5

#solution
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        #check for empty triangle or 1x1 square
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        
        tri = [[1]]
        
        #previous row, we take away 1 as we already have top row from tri
        for i in range(numRows - 1):
            
            #create a temporary pascals triangle to store the zeros/sort the edges
            temp = [0] + tri[-1] + [0]
            
            #build next row
            row = []
            
            #add to next row
            for j in range(len(tri[-1]) + 1):
                row.append(temp[j] + temp[j + 1])
            
            #add new rows to Pascal's triangle
            tri.append(row)
            
        return tri
