"""
@author: Yufei Hu
@date: 01/23/2019
@source: 
"""

from collections import deque

def robot_find_terminal(grid):
    if len(grid) == 0: return None
    if len(grid[0]) == 0: return None
    if grid[0][0] == 0: return None

    seen = set()
    queue = deque()
    queue.append([0, [0, 0]])
    while queue:
        num_steps, pos = queue.popleft()
        y, x = pos
        if (y, x) not in seen:
            seen.add((y, x))
            if grid[y][x] == 9:
                return num_steps
            elif grid[y][x] == 0:
                continue
            else:
                if x + 1 < len(grid[0]):
                    queue.append([num_steps + 1, [y, x + 1]])
                if y + 1 < len(grid):
                    queue.append([num_steps + 1, [y + 1, x]])
    return None

grid = [[1, 0, 0, 1, 1],
        [1, 1, 1, 0, 0],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 9]]
print(robot_find_terminal(grid))
