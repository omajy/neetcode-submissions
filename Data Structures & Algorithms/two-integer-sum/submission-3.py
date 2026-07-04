class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        my_dict = {}

        results = []

        for index, num in enumerate(nums):
            missing = target - num

            if missing in my_dict:
                results.append(my_dict[missing])
                results.append(index)
            
            my_dict[num] = index

        return results