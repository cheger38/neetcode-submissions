def getSeqLen(nums, start):
    seqLen = 1

    i = start + 1
    while i in nums:
        i += 1
        seqLen += 1

    return seqLen

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        maxSeqLen = 0
        for n in numSet:
            if n-1 not in numSet:
                seqLen = getSeqLen(nums, n)
                if seqLen > maxSeqLen:
                    maxSeqLen = seqLen

        
        return maxSeqLen



