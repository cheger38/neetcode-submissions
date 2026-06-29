from collections import defaultdict

def findSubBoxNum(i, j):
    num = 0

    if 0 <= i < 3:
        num = 0
    elif 3 <= i < 6:
        num = 3
    elif 6 <= i < 9:
        num = 6
    
    if 0 <= j < 3:
        num += 0
    elif 3 <= j < 6:
        num += 1
    elif 6 <= j < 9:
        num += 2

    return num

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        subBoxes = defaultdict(set)
        rows = defaultdict(set)
        cols = defaultdict(set)

        for i, row in enumerate(board):
            for j, num in enumerate(row):
                if num == '.':
                    continue
                    
                if num in rows[i]:
                    return False
                if num in cols[j]:
                    return False
                subBox = findSubBoxNum(i, j)
                if num in subBoxes[subBox]:
                    return False

                rows[i].add(num)
                cols[j].add(num)
                subBoxes[subBox].add(num)


        return True
