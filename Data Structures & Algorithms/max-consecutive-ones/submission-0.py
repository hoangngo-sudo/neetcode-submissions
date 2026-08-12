class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_val = 0
        for num in nums:
            if num == 1:
                count += 1
                max_val = max(max_val, count)
            else:
                count = 0
        return max_val