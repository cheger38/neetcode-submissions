class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1

        while True:
            n1, n2 = numbers[i], numbers[j]
            if n1 + n2 == target:
                return [i + 1, j + 1] 

            if n1 + n2 > target:
                j -= 1 
            else:
                i += 1