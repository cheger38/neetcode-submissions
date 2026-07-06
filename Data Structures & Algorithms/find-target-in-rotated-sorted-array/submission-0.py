def findStart(nums):
    lo = 0
    hi = len(nums) - 1

    while lo < hi:
        mid = (lo + hi) // 2

        if nums[mid] > nums[hi]:
            lo = mid + 1
        else:
            hi = mid

    return lo

def rotate(i:int, s:int, n:int):
    return (i + s) % n


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s = findStart(nums)
        n = len(nums)
        
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            i = rotate(mid, s, n)

            if nums[i] == target:
                return i
            elif nums[i] < target:
                lo = mid + 1
            else:
                hi = mid - 1
    
        return -1
        