class Solution:
    def canJump(self, nums: List[int]) -> bool:

        goal = len(nums) - 1
        position = goal

        home = 0

        if position == 0:
            return True

        while position >= home:
            
            if nums[goal - 1] > 0:
                goal -= 1
            elif goal - position <= nums[position]:
                goal = position
            
            if goal == home:
                return True
            # iterate until position reachs the home
            position -= 1

        return False
