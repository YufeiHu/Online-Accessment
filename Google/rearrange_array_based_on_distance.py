# http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=441935&highlight=%B9%B7%2B%C3%E6


def solve_v1(nums, center):

    if len(nums) == 0: return nums
    if len(nums) == 1: return nums

    left = 0
    right = len(nums) - 1
    mid = None
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == center:
            break
        elif nums[mid] < center:
            left = mid + 1
        else:
            right = mid - 1

    if nums[mid] < center:
        left = mid
        right = mid + 1
    else:
        left = mid - 1
        right = mid

    ans = list()
    while left >= 0 and right < len(nums):
        if abs(nums[left] - center) < abs(nums[right] - center):
            ans.append(nums[left])
            left -= 1
        else:
            ans.append(nums[right])
            right += 1

    if left >= 0: ans.extend(nums[:left+1][::-1])
    if right < len(nums): ans.extend(nums[right:])
    return ans


def solve_v2(nums, center):

    if len(nums) == 0: return nums
    if len(nums) == 1: return nums

    ans = list()
    left = 0
    right = len(nums) - 1
    while left <= right:
        if abs(nums[left] - center) > abs(nums[right] - center):
            ans.append(nums[left])
            left += 1
        else:
            ans.append(nums[right])
            right -= 1

    return ans[::-1]


ans = solve_v2([1, 2, 3, 6], 8)
print(ans)