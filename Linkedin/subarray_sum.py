def solution(nums):
    result = 0
    for i in range(0, len(nums)):
        result += (nums[i] * (i + 1) * (len(nums) - i))
    return result


nums = [2, 6, 9]
print(solution(nums))