def solution(nums):
    if len(nums) <= 1: return None
    ans = float('-inf')
    minimum = float('inf')
    for i in range(len(nums)-1):
        minimum = min(minimum, nums[i])
        ans = max(ans, nums[i+1] - minimum)
    return ans


nums = [2, 1, 6, 4]
print(solution(nums))