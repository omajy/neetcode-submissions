class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        my_dict = {}

        result = []

        for index, num in enumerate(nums):
            searching = target - num
            if searching in my_dict:
                result.append(my_dict[searching])
                result.append(index)
            
            my_dict[num] = index
        
        return result