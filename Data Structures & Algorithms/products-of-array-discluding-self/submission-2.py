class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProd = [1 for _ in range(len(nums))]
        rightProd = [1 for _ in range(len(nums))]

        for i, n in enumerate(nums):
            if i == 0:
                leftProd[i] = n
                continue
            
            leftProd[i] = leftProd[i-1] * n

        for i in reversed(range(len(nums))):
            n = nums[i]
            
            if i == len(nums)-1:
                rightProd[i] = n
                continue

            rightProd[i] = rightProd[i+1] * n

        results = []
        for i, n in enumerate(nums):
            if i == 0:
                results.append(rightProd[i+1])
                continue

            if i == len(nums)-1:
                results.append(leftProd[i-1])
                continue

            results.append(leftProd[i-1] * rightProd[i+1])

        return results

            


            



