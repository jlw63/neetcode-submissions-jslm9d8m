class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        check_set = set()
        for i in nums:
            check_set.add(i)
        longest_count = 0

        for n in check_set:
            count = 0
            if (n - 1) not in check_set:
                while n+count in check_set:
                    count += 1
                if longest_count < count:
                    longest_count = count

        return longest_count

        