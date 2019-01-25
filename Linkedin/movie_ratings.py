def solution(nums):
    if len(nums) == 0: return 0
    if len(nums) == 1: return max(nums[0], 0)
    if len(nums) == 2: return max(nums)
    return max(nums[0] + solution(nums[1:]), nums[1] + solution(nums[2:]))


def maxSumSubarrayRemovingOneEle(arr, n):
    # Maximum sum subarrays in forward and backward
    # directions
    fw = [0 for k in range(n)]
    bw = [0 for k in range(n)]

    # Initialize current max and max so far.
    cur_max, max_so_far = arr[0], arr[0]

    # calculating maximum sum subarrays in forward
    # direction
    for i in range(n):
        cur_max = max(arr[i], cur_max + arr[i])
        max_so_far = max(max_so_far, cur_max)

        # storing current maximum till ith, in
        # forward array
        fw[i] = cur_max

        # calculating maximum sum subarrays in backward
    # direction
    cur_max = max_so_far = bw[n - 1] = arr[n - 1]
    i = n - 2
    while i >= 0:
        cur_max = max(arr[i], cur_max + arr[i])
        max_so_far = max(max_so_far, cur_max)

        # storing current maximum from ith, in
        # backward array
        bw[i] = cur_max
        i -= 1

    #  Initializing final ans by max_so_far so that,
    #  case when no element is removed to get max sum
    #  subarray is also handled
    fans = max_so_far

    #  choosing maximum ignoring ith element
    for i in range(1, n - 1):
        fans = max(fans, fw[i - 1] + bw[i + 1])

    return fans


nums = [-2, -3, 4, -1, -2, 1, 5, -3]
print(solution(nums))
print(maxSumSubarrayRemovingOneEle(nums, len(nums)))