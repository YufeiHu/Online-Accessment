from collections import Counter


def solution(nums):
    cnt = Counter(nums)
    ans = 0
    cur = -1
    for k in sorted(cnt.keys()):
        cur = max(cur, k)
        while cnt[k]:
            ans += cur
            cur += 1
            cnt[k] -= 1
    return ans


nums = [3, 2, 1, 2, 7]
print(solution(nums))