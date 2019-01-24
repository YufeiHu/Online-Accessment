"""
@author: Yufei Hu
@date: 01/23/2019
@source: 
"""

def find_substrings_with_k_distinct_letters(string, k):
    ans = set()
    for i in range(len(string)):
        letters_memo = [0] * 26
        num_distinct = 0
        for j in range(i, len(string)):
            index = ord(string[j]) - ord('a')
            letters_memo[index] += 1
            if letters_memo[index] == 1:
                num_distinct += 1

            if num_distinct == k:
                ans.add(string[i: j + 1])
            elif num_distinct > k:
                break
    return ans

string = "abcdabc"
k = 3
print(find_substrings_with_k_distinct_letters(string, k))
