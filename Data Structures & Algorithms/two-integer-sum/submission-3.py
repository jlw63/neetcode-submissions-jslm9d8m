class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}
        #nums[i] + nums[j] == target
        #rearrange
        #nums[j] == target - num[i]



        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in hashmap:
                return [hashmap[compliment], i]
            hashmap[nums[i]] = i