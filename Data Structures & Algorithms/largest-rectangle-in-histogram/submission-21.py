class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # stores pairs: (start_index, height)
        maxArea = 0

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                area = height * (i - index)
                maxArea = max(maxArea, area)

                start = index

            stack.append((start, h))

        n = len(heights)

        while stack:
            index, height = stack.pop()
            area = height * (n - index)
            maxArea = max(maxArea, area)

        return maxArea