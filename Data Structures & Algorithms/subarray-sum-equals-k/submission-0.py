class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap={0:1}
        count = 0
        prefix = 0
        for n in nums:
            prefix += n
            count += hashmap.get(prefix - k, 0)
            hashmap[prefix] = hashmap.get(prefix,0) + 1
        return count
        