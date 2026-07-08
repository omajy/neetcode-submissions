class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
       
        left = 0
        right = len(matrix[0]) - 1

        top = 0
        bottom = len(matrix) - 1

        result = []

        phase = 0

        while left <= right and top <= bottom:
            
            if phase % 2 == 0:
                # go right then down
                # update top 
                # update right

                # append top left to right
                for index in range(left, right + 1):
                    result.append(matrix[top][index])
                top += 1
                # append right side from updated top to bottom
                for index in range(top, bottom + 1):
                    result.append(matrix[index][right])
                right -= 1


            else:
                # go left then up
                # update bottom
                # update left

                # append bottom right to left
                for index in range(right, left - 1, -1):
                    result.append(matrix[bottom][index])
                bottom -= 1
                # append left side from updated bottom to top
                for index in range(bottom, top - 1, -1):
                    result.append(matrix[index][left])
                left += 1

            phase += 1

        return result