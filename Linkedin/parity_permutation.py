def isEven(n):
    return n % 2 == 0


def accept(nums):
    for i in range(0, len(nums), 2):
        if i - 1 >= 0:
            if isEven(nums[i-1]) and isEven(nums[i]):
                return False
            if not isEven(nums[i-1]) and not isEven(nums[i]):
                return False
        if i + 1 < len(nums):
            if isEven(nums[i]) and isEven(nums[i+1]):
                return False
            if not isEven(nums[i]) and not isEven(nums[i+1]):
                return False
    return True


def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if len(nums) == 0: return []
    if len(nums) == 1: return [[nums[0]]]

    element = nums.pop()
    result_curr = permute(nums)
    result_next = []
    for i in range(len(result_curr)):
        for j in range(len(result_curr[0]) + 1):
            result = list(result_curr[i])
            result.insert(j, element)
            result_next.append(result)
    return result_next


def solution(n):
    nums = list(range(1, n+1))
    results = permute(nums)
    ans = list()
    for result in results:
        if accept(result):
            ans.append(result)
    ans = sorted(ans)
    return ans


print(solution(5))