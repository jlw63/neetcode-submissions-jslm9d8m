class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i], 0) + 1
        bucket = [[]for _ in range(len(nums) + 1)]

        for nums, count in freq.items():
            bucket[count].append(nums)
        
        ans = []
        for i in range(len(bucket) -1, -1 , -1):
            for n in bucket[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans

        