class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        check = set(nums)
        longest = 0
        for n in nums:
            if (n-1) in check:
                continue
            else:
                counter = 1
                while (n + counter) in check:
                    counter += 1
                longest = max(counter, longest)
        return longest
