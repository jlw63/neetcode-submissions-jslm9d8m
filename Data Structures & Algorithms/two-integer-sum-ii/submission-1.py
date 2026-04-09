class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #formula: index1 + index2 = target
        #rearrange to find index 2 = target - index1 = index2
        #check like this?


        for i in range(len(numbers)):
            value1 = numbers[i]
            need = target - value1
            for j in range(i + 1, len(numbers)):
                value2 = numbers[j]
                if value2 == need:

                    return [i+1,j+1]
            




        