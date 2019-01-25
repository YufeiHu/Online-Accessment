def solve(s, t):

    ans = list()
    for i in range(len(t) + 1):
        if i == 0:
            ans.append([1] * (len(s) + 1))
        else:
            ans.append([0] * (len(s) + 1))

    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j] and (i > 0 and s[i] != s[i-1]):
                ans[j + 1][i + 1] = ans[j + 1][i] + ans[j][i]
            else:
                ans[j + 1][i + 1] = ans[j + 1][i]

    return ans[-1][-1]


print(solve("acbccapt", "cat"))