def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        prev = float('inf')

        for i in range(len(matrix)):

            for j in range(len(matrix[0])):
                if matrix[i][j] == target:
                    return True

                if matrix[i][j] > target:
                    break
            
            prev = matrix[i][len(matrix[0])-1]
            
            if target < prev:
                return False

        return False