"""
@author: Yufei Hu
@date: 01/23/2019
@source: 
"""

def two_sum_smaller_than_k(nums, target):
    nums = sorted(nums)

    target_actual = float('-inf')
    i = 0
    j = len(nums) - 1
    while i < j:
        sum_cur = nums[i] + nums[j]
        if sum_cur <= target:
            target_actual = max(target_actual, sum_cur)
            i += 1
        else:
            j -= 1

    ans = list()
    if target_actual != float('-inf'):
        i = 0
        j = len(nums) - 1
        while i < j:
            sum_cur = nums[i] + nums[j]
            if sum_cur == target_actual:
                ans.append([nums[i], nums[j]])
                i += 1
                j -= 1
            elif sum_cur < target_actual:
                i += 1
            else:
                j -= 1
    return ans

nums = [50, 10, 30, 40, 70]
print(two_sum_smaller_than_k(nums, 84))
