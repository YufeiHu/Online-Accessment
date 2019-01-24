"""
@author: Yufei Hu
@date: 01/23/2019
@source: Leetcode-48
"""

class Solution:
    def rotate_help(self, matrix, k):
        n = len(matrix)
        i_start = k
        i_end = n - 1 - k
        num = i_end - i_start
        
        tmp1 = list()
        for i in range(num):
            tmp1.append(matrix[i_end - i][i_end])
            matrix[i_end - i][i_end] = matrix[i_start][i_end - i]
        
        tmp2 = list()
        for i in range(num):
            tmp2.append(matrix[i_end][i_start + i])
            matrix[i_end][i_start + i] = tmp1[i]
        
        for i in range(num):
            tmp1[i] = matrix[i_start + i][i_start]
            matrix[i_start + i][i_start] = tmp2[i]
        
        for i in range(num):
            matrix[i_start][i_end - i] = tmp1[i]
            
        if k == int((n - 1) / 2):
            return
        else:
            self.rotate_help(matrix, k + 1)

    def rotate(self, matrix):
        n = len(matrix)
        if n == 0 or n == 1:
            return
        else:
            self.rotate_help(matrix, 0)
