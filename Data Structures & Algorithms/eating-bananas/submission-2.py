from math import ceil
def can(piles, h, k):
    for p in piles:
        h -= ceil(p / k)

    if h < 0:
        return False
    else:
        return True


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        lo = 1
        hi = max(piles)

        while lo < hi:
            mid = (lo + hi) // 2

            if can(piles, h, mid):
                hi = mid
            else:
                lo = mid + 1

        return lo

            
