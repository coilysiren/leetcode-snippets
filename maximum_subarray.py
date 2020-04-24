# https://leetcode.com/problems/maximum-subarray/submissions/


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        numberOfElements = len(nums)
        globalMax = localMax = nums[0]

        for i in range(1, numberOfElements):

            localMax = localMax + nums[i]
            globalMax = max(localMax, globalMax)
            localMax = max(globalMax, localMax)
