"""
@author: Yufei Hu
@date: 01/23/2019
@source: 
"""

import heapq

def compute_rating(ratings):
    ans = list()
    for ID, rates in ratings:
        rates_heap = [x * (-1) for x in rates]
        heapq.heapify(rates_heap)
        rate_avg = 0
        num_rate = 0
        for i in range(min(5, len(rates))):
            rate_avg += (heapq.heappop(rates_heap) * -1)
            num_rate += 1
        if num_rate != 0:
            rate_avg /= num_rate
        ans.append([ID, rate_avg])
    return ans

ratings = [[0, [5, 3, 1, 7, 9, 11, 2]],
           [1, [1, 3, 1, 7]],
           [2, []]]
print(compute_rating(ratings))
