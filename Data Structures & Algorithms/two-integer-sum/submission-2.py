class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dif = dict()

        for i, x in enumerate(nums):
            if target - x in dif:
                return [min(i, dif[target - x]), max(i, dif[target - x])]
            else:
                dif[x] = i

        return []


