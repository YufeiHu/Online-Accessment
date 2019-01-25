def solution(string):

    ans = ""
    for i in range(len(string)):
        ans = max(ans, string[i:])
    return ans


print(solution("gggaaagggggggggg"))