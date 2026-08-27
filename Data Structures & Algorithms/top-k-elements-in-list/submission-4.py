from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(0, len(nums)+1)]

        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1

        for key, val in freq.items():
            buckets[val].append(key)
            
        topK = []
        for bucket in reversed(buckets):
            if not bucket:
                continue

            if len(bucket) < k:
                topK.extend(bucket)
                k -= len(bucket)
            else:
                topK.extend(bucket[0:k])
                break

        return topK


