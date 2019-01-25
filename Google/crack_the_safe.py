class Solution(object):

    def __init__(self):
        self.ans = ""

    def DFS(self, node, visited, k):
        for num in map(str, range(k)):
            nodeCur = node + num
            if nodeCur not in visited:
                visited.add(nodeCur)
                self.DFS(nodeCur[1:], visited, k)
                self.ans += num

    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        node = "0" * (n - 1)
        visited = set()
        self.DFS(node, visited, k)
        return self.ans + "0" * (n - 1)


mySolution = Solution()
print(mySolution.crackSafe(3, 2))