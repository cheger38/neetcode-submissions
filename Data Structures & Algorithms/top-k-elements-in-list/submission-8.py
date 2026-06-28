from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1

        order = []
        for n, f in freq.items():
            order.append((f, n))
        order.sort()
        
        return [x[1] for x in order[-k:]]
            
            
        
