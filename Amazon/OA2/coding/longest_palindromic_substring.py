"""
@author: Yufei Hu
@date: 01/23/2019
@source: Leetcode-5
"""

class Solution:
    def getPalindrome(self, s, l, r):
        if r >= len(s): return l, r - 1
        if s[l] != s[r]: return l, r - 1
        while l >= 0 and r < len(s):
            if s[l] == s[r]:
                l -= 1
                r += 1
            else:
                break
        return l + 1, r - 1
    
    def longestPalindrome(self, s):
        ans = ""
        for i in range(len(s)):
            l, r = self.getPalindrome(s, i, i)
            if r - l + 1 > len(ans):
                ans = s[l: r + 1]
            l, r = self.getPalindrome(s, i, i + 1)
            if r - l + 1 > len(ans):
                ans = s[l: r + 1]
        return ans
