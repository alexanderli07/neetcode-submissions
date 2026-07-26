class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            if nums[i] in nums[i+1:]:
                return True
            else:
                continue
        return False


