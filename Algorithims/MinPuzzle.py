from collections import deque


def minEffort(puzzle):

    m = len(puzzle)
    n = len(puzzle[0])

    que = deque()

    que.append((0, 0, puzzle[0][0]))

    efforts = [[float('inf')] * n for _ in range(m)]
    efforts[0][0] = 0

    while que:
        row, col, prevHeight = que.popleft()

        if row == m - 1 and col == n - 1:
            return efforts[row][col]

        neighbors = [(row - 1, col), (row + 1, col),
                     (row, col - 1), (row, col + 1)]

        for adjRow, adjCol in neighbors:
            if 0 <= adjRow < m and 0 <= adjCol < n:
                currHeight = puzzle[adjRow][adjCol]
                newEffort = max(efforts[row][col], abs(
                    currHeight - prevHeight))

                if newEffort < efforts[adjRow][adjCol]:
                    efforts[adjRow][adjCol] = newEffort
                    que.append((adjRow, adjCol, currHeight))

    return -1


7
