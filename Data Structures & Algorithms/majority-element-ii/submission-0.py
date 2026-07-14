class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        output = []
        for n in nums:
            count[n] = count.get(n,0) + 1
        for num, cnt in count.items():
            if (cnt) > (len(nums)//3):
                output.append(num)

        return output

        