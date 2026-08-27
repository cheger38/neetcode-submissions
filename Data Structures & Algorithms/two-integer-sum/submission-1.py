class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difs = dict()

        for i, n in enumerate(nums):
            dif = target - n
            if dif in difs:
                return [min(i, difs[dif]), max(i, difs[dif])]
            else:
                difs[n] = i

        return []