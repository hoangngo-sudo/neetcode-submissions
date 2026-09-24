class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        haveSeen = set()
        for num in nums:
            if num in haveSeen:
                return True
            else:
                haveSeen.add(num)
        return False