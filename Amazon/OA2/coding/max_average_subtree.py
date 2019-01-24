"""
@author: Yufei Hu
@date: 01/23/2019
@source: 
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def __init__(self):
        self.avg = float('-inf')
        self.node = None

    def findSubtree2(self, root):
        if root is None:
            return None
        self.getSubtree(root)
        return self.node

    def getSubtree(self, root):
        if root is None:
            return 0, 0

        sumLeft, countLeft = self.getSubtree(root.left)
        sumRight, countRight = self.getSubtree(root.right)

        sumRoot = sumLeft + sumRight + root.val
        countRoot = countLeft + countRight + 1

        average = sumRoot * 1.0 / countRoot
        if self.node is None or average > self.avg:
            self.avg = average
            self.node = root

        return sumRoot, countRoot

root = TreeNode(1)
r1 = TreeNode(2)
r2 = TreeNode(3)
r3 = TreeNode(2)
r4 = TreeNode(1)
r5 = TreeNode(1)
root.left = r1
root.right = r2
r1.left = r3
r2.left = r4
r2.right = r5
mySolution = Solution()
print(mySolution.findSubtree2(root).val)
