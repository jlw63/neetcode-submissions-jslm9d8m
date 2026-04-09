class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set(nums)
        longest = 0

        for i in range(len(nums)):
            if (nums[i] -1) not in hs:
                start = nums[i]
                length = 0
                while start in hs:
                    start += 1
                    length += 1
                longest = max(longest, length)
        return longest

        