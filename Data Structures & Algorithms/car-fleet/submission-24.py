def willMeet(car1: int, car2: int, target: int, position: List[int], speed: List[int]):
    leadCar = None
    trailCar = None

    if position[car1] > position[car2]:
        leadCar = car1
        trailCar = car2
    else:
        leadCar = car2
        trailCar = car1

    leadCarTime = (target - position[leadCar]) / speed[leadCar]
    trailCarTime = (target - position[trailCar]) / speed[trailCar]

    print("Leadcar pos:", position[leadCar])
    print("Leadcar spd:", speed[leadCar])
    print("Leadcar time:", leadCarTime)
    print()
    print("Trailcar pos:", position[trailCar])
    print("Trailcar spd:", speed[trailCar])
    print("Trailcar time:", trailCarTime)
    print('\n')

    if leadCarTime >= trailCarTime: 
        return True
    else:
        return False


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        timeToTarget = []

        order = [(p, i) for i, p in enumerate(position)]
        order.sort(reverse=True)

        stack = []

        for p, i in order:
            time = (target - position[i]) / speed[i]

            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)

