"""
@author: Yufei Hu
@date: 01/23/2019
@source: Leetcode-409
"""

from collections import Counter

class Solution:
    def longestPalindrome(self, s):
        ans = 0
        flag_odd = 0
        memo = Counter(s)
        for cnt in memo.values():
            if cnt % 2 == 0:
                ans += cnt
            else:
                ans += (cnt - 1)
                flag_odd = 1
        ans += flag_odd
        return ans
