from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for n, f in freq.items():
            buckets[f].append(n)

        answer = []
        count = 0
        for b in buckets[::-1]:
            if not b:
                continue
            
            if len(b) < k - count:
                count += len(b)
                answer += b
            else:
                answer += b[:k-count]
                break
                
        return answer