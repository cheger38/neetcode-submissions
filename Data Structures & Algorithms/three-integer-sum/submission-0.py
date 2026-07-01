class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)     

        result = []
        for i, n in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -n
            j = i + 1
            k = len(nums) - 1
            while j < k:
                twoSum = nums[j] + nums[k]
                if twoSum == target:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif twoSum < target:
                    j += 1
                elif twoSum > target:
                    k -= 1


        return result