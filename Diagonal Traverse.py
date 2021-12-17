#example input
matrix = [[1,2],[3,4]]

#solution
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        
        #check if matrix is empty
        if not matrix or not matrix[0]:
            return []
        
        num_rows, num_cols = len(matrix), len(matrix[0])
        
        #a matrix has num_rows + num_cols - 1 diagonals
        diagonals = [[] for a in range(num_rows + num_cols - 1)]
        
        #iterate through each position of the matrix
        for i in range(num_rows):
            for j in range(num_cols):
                diagonals[i + j].append(matrix[i][j])
        
        #next smallest possible matrix is a 1x1 matrix
        res = diagonals[0]
        
        #if matrix is bigger then loop through the other diagonals
        for x in range(1, len(diagonals)):
            
            #for standard diagonals we want the regular direction
            if x % 2 == 1:
                res.extend(diagonals[x])
            
            #if we are dealing with the 'even-th' diagonal we will reverse it
            else:
                res.extend(diagonals[x][::-1])
        
        #return matrix in diagonal order
        return res
