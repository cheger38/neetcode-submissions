class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = [-1 for _ in range(len(height))]
        rightMax = [-1 for _ in range(len(height))]

        for i, n in enumerate(height):
            if i == 0:
                leftMax[i] = n
            else:
                leftMax[i] = max(n, leftMax[i-1])
        
        for i, n in reversed(list(enumerate(height))):
            if i == len(height) - 1:
                rightMax[i] = n
            else:
                rightMax[i] = max(n, rightMax[i+1])
            
        area = 0    
        for i, n in enumerate(height):
            if i == 0 or i == len(height) - 1:
                continue
            barArea = min(leftMax[i-1], rightMax[i+1]) - n
            print("Bararea for", i , "is", barArea)
            if barArea > 0:
                area += barArea

            
        print(leftMax)
        print(rightMax)

        return area
