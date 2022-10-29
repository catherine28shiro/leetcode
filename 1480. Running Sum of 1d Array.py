"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
"""
"""
:type nums: List[int]
:rtype: List[int]
"""
"""
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4]
"""
# using input array for output
class Solution(object):
    def runningSum(self, nums):
        l = len(nums)
        for i in range(1,l):
            nums[i] += nums[i-1]
        return nums

