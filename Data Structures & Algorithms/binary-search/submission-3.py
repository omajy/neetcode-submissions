class Solution:
    def search(self, nums: List[int], target: int) -> int:

        begin = 0

        end = len(nums) - 1

        middle = begin + (end - begin) // 2

        while begin <= end:
            
            middle = begin + (end - begin) // 2
            
            if target > nums[middle]:
                begin = middle + 1
            elif target < nums[middle]:
                end = middle - 1
            else:
                return nums.index(target)
        
        return -1