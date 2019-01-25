from collections import defaultdict


def solution(strings):

    memo = defaultdict(int)
    for i, string in enumerate(strings):
        if string in memo:
            strings[i] += str(memo[string])
            memo[string] += 1
        else:
            memo[string] += 1
    return strings


A = ["alex", "ben", "alice", "alex", "alice"]
print(solution(A))