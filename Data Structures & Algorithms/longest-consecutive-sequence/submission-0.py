def getSeqLen(start, nums):
    seqLen = 1
    while start + 1 in nums:
        seqLen += 1
        start += 1

    return seqLen


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maxSeqLen = 0

        for n in nums:
            if n-1 not in nums:
                seqLen = getSeqLen(n, nums)

                maxSeqLen = max(maxSeqLen, seqLen)
            

        return maxSeqLen