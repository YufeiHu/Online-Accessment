"""
@author: Yufei Hu
@date: 01/23/2019
@source: 
"""

from collections import deque

def max_min_path(grid):
    if len(grid) == 0: return 0
    if len(grid[0]) == 0: return 0

    dp = list()
    for y in range(len(grid)):
        dp.append([0] * len(grid[0]))
    dp[0][0] = grid[0][0]
    print(dp)

    for y in range(1, len(grid)):
        dp[y][0] = min(dp[y - 1][0], grid[y][0])
    print(dp)

    for x in range(1, len(grid[0])):
        dp[0][x] = min(dp[0][x - 1], grid[0][x])
    print(dp)

    for y in range(1, len(grid)):
        for x in range(1, len(grid[0])):
            dp[y][x] = min(max(dp[y - 1][x], dp[y][x - 1]), grid[y][x])
    print(dp)

    return dp[-1][-1]

grid = [[5, 10, 2, 5, 6],
        [4, 1, 2, 10, 20],
        [20, 5, 3, 20, 11],
        [11, 1, 2, 1, 10]]
print(max_min_path(grid))
