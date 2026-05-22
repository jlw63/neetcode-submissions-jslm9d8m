class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums)
        for count, nums in enumerate(nums):
            result ^= count
            result ^= nums
        return result