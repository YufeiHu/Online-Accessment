"""
@author: Yufei Hu
@date: 01/24/2019
@source: 
"""

def is_valid(status):
    for cnt in status:
        if cnt != 0 and cnt != 1:
            return False
    return True

def subStringsKDist(string, k):
    if len(string) < k:
        return list()
    
    ans = set()
    status = [0] * 26
    for i in range(k):
        index = ord(string[i]) - ord('a')
        status[index] += 1
    if is_valid(status):
        ans.add(string[0: k])
    
    l = 0
    while l + k < len(string):
        index = ord(string[l]) - ord('a')
        status[index] -= 1
        index = ord(string[l + k]) - ord('a')
        status[index] += 1
        if is_valid(status):
            ans.add(string[l + 1: l + 1 + k])
        l += 1
        
    return list(ans)
