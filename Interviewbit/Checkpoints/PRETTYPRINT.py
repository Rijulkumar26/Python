class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
        array_size = A * 2 - 1 
        result = [[0 for i in range(array_size)] for j in range(array_size)] 

        for row in range(array_size): 
            for col in range(array_size): 
                mid = array_size // 2
                abs_val_from_row = abs(row - mid) + 1 
                abs_val_from_col = abs(col - mid) + 1 

                result[row][col] = max(abs_val_from_row, abs_val_from_col)
                
        return result