def twoToOne(i: int, j: int, m: int, n: int):
    return i * m + j

def oneToTwo(i: int, m: int, n: int):
    return (i // n, i % n)


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        lo = 0
        hi = m * n - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            i, j = oneToTwo(mid, m, n)
            print(mid, i, j)

            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                hi = mid - 1
            else:
                lo = mid + 1

        return False
        