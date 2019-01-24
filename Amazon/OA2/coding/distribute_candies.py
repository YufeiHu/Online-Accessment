"""
@author: Yufei Hu
@date: 01/23/2019
@source: Leetcode-575
"""

class Solution:
    def distributeCandies(self, candies):
        memo = set()
        for candy in candies:
            memo.add(candy)
        return int(min(len(candies) / 2, len(memo)))
