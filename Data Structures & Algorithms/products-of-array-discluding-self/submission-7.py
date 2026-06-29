class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [0 for _ in range(len(nums))]
        for i, n in enumerate(nums):
            if i == 0:
                pref[i] = n
                continue
            pref[i] = pref[i-1] * n

        suff = [0 for _ in range(len(nums))]
        for i, n in reversed(list(enumerate(nums))):
            if i == len(nums) - 1:
                suff[i] = n
                continue
            suff[i] = suff[i+1] * n
        
        result = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            if i == 0:
                result[i] = suff[i+1]
            elif i == len(nums) - 1:
                result[i] = pref[i-1]
            else:
                result[i] = pref[i-1] * suff[i+1]

        return result

