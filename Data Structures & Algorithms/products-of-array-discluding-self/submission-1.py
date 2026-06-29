class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numZeros = 0
        prod = 1

        for n in nums:
            if n != 0:
                prod *= n
            else:
                numZeros += 1

        result = []
        if numZeros > 1:
            return [0 for _ in range(len(nums))]
        elif numZeros == 1:
            for n in nums:
                if n != 0:
                    result.append(0)
                else:
                    result.append(prod)
        else:
            for n in nums:
                result.append(prod//n)
    

        print(result)
        return result


        