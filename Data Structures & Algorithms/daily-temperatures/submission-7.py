class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for _ in range(len(temperatures))]
        stack = []
    
        for i, n in enumerate(temperatures):
            if not stack or temperatures[stack[-1]] > n:
                stack.append(i)
            else:
                while stack and temperatures[stack[-1]] < n:
                    j = stack.pop()
                    result[j] = i - j

                stack.append(i)

        return result
