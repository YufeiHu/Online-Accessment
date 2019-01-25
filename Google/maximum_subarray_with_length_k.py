class Solution(object):
    def maxSubArrayWithLengthK(self, nums, k):
        if len(nums) < k: return 0
        curSum = sum(nums[0:k])
        ans = curSum
        for i in range(1, len(nums)-k+1):
            curSum = curSum - nums[i-1] + nums[i+k-1]
            ans = max(ans, curSum)
        return ans


inputs = [1,2,4,6,-1,2,1,20]
mySolution = Solution()
print(mySolution.maxSubArrayWithLengthK(inputs, 3))