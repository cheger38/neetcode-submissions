class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, i) for i, p in enumerate(position)]
        cars.sort(reverse=True)
                    
        stack = []

        for p, i in cars:
            time = (target - position[i]) / speed[i]

            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)