class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        
        mArea = 0
        while i < j:
            area = (j - i) * min(heights[i], heights[j])
            mArea = max(area, mArea)

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        
        
        return mArea
