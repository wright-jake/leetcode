#example input
matrix = [[1,2,3],[4,5,6],[7,8,9]]

#solution
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        #check if matrix is empty
        if not matrix:
            return []
        
        start_row, end_row, start_col, end_col = 0, len(matrix), 0, len(matrix[0])
        
        spiral = []
        
        while start_row < end_row or start_col < end_col:
            
            #right
            if start_row < end_row:
                spiral.extend([matrix[start_row][i] for i in range(start_col, end_col)])
                start_row += 1
            
            #down
            if start_col < end_col:
                spiral.extend([matrix[i][end_col - 1] for i in range(start_row, end_row)])
                end_col -= 1
            
            #left
            if start_row < end_row:
                spiral.extend([matrix[end_row - 1][i] for i in range(end_col - 1, start_col - 1, -1)])
                end_row -= 1
            
            #up
            if start_col < end_col:
                spiral.extend([matrix[i][start_col] for i in range(end_row - 1, start_row - 1, -1)])
                start_col += 1
            
        return spiral
