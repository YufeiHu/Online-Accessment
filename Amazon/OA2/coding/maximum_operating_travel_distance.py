"""
@author: Yufei Hu
@date: 01/23/2019
@source: 
"""

def maximum_operating_travel_distance(routes_A, routes_B, target):
    routes_A = sorted(routes_A)
    routes_B = sorted(routes_B)
    i = len(routes_A) - 1
    j = len(routes_B) - 1
    while i >= 0 and j >= 0:
        sum_cur = routes_A[i] + routes_B[j]
        if sum_cur <= target:
            return [routes_A[i], routes_B[j]]
        else:
            if i > 0:
                sum_left = routes_A[i - 1] + routes_B[j]
            else:
                sum_left = float('-inf')

            if j > 0:
                sum_right = routes_A[i] + routes_B[j - 1]
            else:
                sum_right = float('-inf')

            if sum_left < sum_right:
                j -= 1
            else:
                i -= 1

    return list()

routes_A = [50, 60, 70, 80, 80]
routes_B = [20, 30, 30, 40]
print(maximum_operating_travel_distance(routes_A, routes_B, 65))
