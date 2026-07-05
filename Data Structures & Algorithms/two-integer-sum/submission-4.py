class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        my_dict = {}

        for index, num in enumerate(nums):
            missing = target - num

            if missing in my_dict: 
                return [my_dict[missing], index]
            
            my_dict[num] = index

        return []