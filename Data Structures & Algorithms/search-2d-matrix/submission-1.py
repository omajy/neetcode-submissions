class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        matrix_elongated = []
        
        for row in matrix:
            matrix_elongated += row

        left = 0
        right = len(matrix_elongated) - 1
        middle = right - left // 2

        while left <= right:
            
            middle = right - left // 2
            
            if target < matrix_elongated[middle]:
                right = middle - 1
            elif target > matrix_elongated[middle]:
                left = middle + 1
            else:
                return True

        return False
