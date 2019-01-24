"""
@author: Yufei Hu
@date: 01/23/2019
@source: Leetcode-819
"""

from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph, banned):
        words = list()
        symbols = {"!", "?", "'", ",", ";", ".", " "}
        
        i = 0
        while i < len(paragraph):
            if paragraph[i] in symbols:
                i += 1
            else:
                j = i + 1
                while j < len(paragraph) and paragraph[j] not in symbols:
                    j += 1
                word = paragraph[i:j].lower()
                if word not in banned:
                    words.append(word)
                i = j
        
        cnt_max = 0
        ans = ""
        memo = Counter(words)
        for word, cnt in memo.items():
            if cnt > cnt_max:
                cnt_max = cnt
                ans = word
        return ans
