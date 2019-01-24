"""
@author: Yufei Hu
@date: 01/23/2019
@source: Leetcode-490
"""

from collections import deque

class Solution:
    def hasPath(self, maze, start, destination):
        if len(maze) == 0: return False
        if len(maze[0]) == 0: return False
        
        stack = list()
        stack.append(tuple(start))
        seen = set()
        move = ((-1, 0), (1, 0), (0, -1), (0, 1))
        
        while stack:
            pos = stack.pop()
            if pos not in seen:
                seen.add(pos)
                if pos == tuple(destination):
                    return True
                y, x = pos
                for dy, dx in move:
                    y_next = y + dy
                    x_next = x + dx
                    while 0 <= y_next and y_next < len(maze) and 0 <= x_next and x_next < len(maze[0]) and maze[y_next][x_next] == 0:
                        y_next += dy
                        x_next += dx
                    y_next -= dy
                    x_next -= dx
                    stack.append((y_next, x_next))
            
        return False
