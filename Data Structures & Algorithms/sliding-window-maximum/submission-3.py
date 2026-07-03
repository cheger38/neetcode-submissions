from heapq import heappop, heappush

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        result = []
        heap = []
        for i, n in enumerate(nums):
            heappush(heap, (-n, i))

            l = i - k + 1

            while heap[0][1] < l:
                heappop(heap)

            if l >= 0:
                result.append(-heap[0][0])

        return result



