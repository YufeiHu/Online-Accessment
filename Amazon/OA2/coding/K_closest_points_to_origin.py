"""
@author: Yufei Hu
@date: 01/23/2019
@source: Leetcode-973
"""

import heapq

class Solution:
    def kClosest(self, points, K):
        if K == 0:
            return list()
        
        distance = list()
        for point in points:
            distance_cur = [point[0] ** 2 + point[1] ** 2]
            distance.append([distance_cur, point])
        
        heapq.heapify(distance)
        ans = list()
        for _ in range(min(len(distance), K)):
            ans.append(heapq.heappop(distance)[1])
        return ans
