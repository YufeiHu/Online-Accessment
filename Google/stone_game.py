def helper(memo, nums, i, j):
    if i > j: return 0
    if j == i: return nums[i]
    if (i, j) in memo: return memo[(i, j)]

    ans1 = nums[i] + min(helper(memo, nums, i + 2, j), helper(memo, nums, i + 1, j - 1))
    ans2 = nums[j] + min(helper(memo, nums, i + 1, j - 1), helper(memo, nums, i, j - 2))
    memo[(i, j)] = max(ans1, ans2)
    return memo[(i, j)]


def stoneGame(piles):
    """
    :type piles: List[int]
    :rtype: bool
    """
    memo = dict()
    ans1 = helper(memo, piles, 0, len(piles) - 1)
    ans2 = sum(piles) - ans1
    return ans1 > ans2


print(stoneGame(
    [59, 48, 36, 70, 59, 93, 60, 98, 15, 32, 31, 13, 27, 14, 8, 17, 4, 76, 24, 47, 39, 81, 26, 6, 70, 73, 8, 36, 71, 19,
     66, 61, 86, 63, 97, 32, 15, 36, 68, 69, 32, 53, 83, 35, 100, 41, 44, 8, 28, 76, 39, 90, 37, 35, 11, 99, 48, 49, 64,
     74, 6, 54, 12, 99, 34, 47, 78, 36, 51, 26, 43, 83, 10, 68, 32, 48, 72, 54, 64, 64, 44, 62, 77, 60, 100, 84, 15, 24,
     95, 6, 6, 8, 24, 21, 84, 61, 75, 26, 63, 54]))
