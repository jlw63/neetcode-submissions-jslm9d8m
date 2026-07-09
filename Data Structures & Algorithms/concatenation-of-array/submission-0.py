class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(2):
            for i in nums:
                output.append(i)
        return output
        