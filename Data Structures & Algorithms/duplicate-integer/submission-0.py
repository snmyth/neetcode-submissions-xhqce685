class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        original_length = len(nums)
        setnum = set(nums)
        new_length = len(setnum)
        if new_length != original_length:
            return True
        else:
            return False