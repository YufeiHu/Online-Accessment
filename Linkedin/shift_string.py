def solution(string, L, R):
    L = ((L - R) + len(string)) % len(string)
    print(L)
    ans = string[L:] + string[:L]
    return ans


print(solution("abcd", 100, 1985))