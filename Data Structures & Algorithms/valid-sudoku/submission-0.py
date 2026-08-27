from collections import defaultdict

def getBox(i, j):
    i //= 3 
    j //= 3

    return i * 3 + j

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = defaultdict(set)
        rows = defaultdict(set)
        cols = defaultdict(set)

        for i, row in enumerate(board):
            for j, n in enumerate(row):
                if n == '.':
                    continue
                    
                if n in boxes[getBox(i, j)]:
                    return False

                if n in rows[i]:
                    return False

                if n in cols[j]:
                    return False

                boxes[getBox(i, j)].add(n)
                rows[i].add(n)
                cols[j].add(n)

        return True

