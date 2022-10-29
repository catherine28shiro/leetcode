"""
Given an array of integers nums, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers strictly to the left of the 
index is equal to the sum of all the numbers strictly to the index's right.
"""

"""
Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
"""
"""
:type nums: List[int]
:rtype: int
"""
import math

class Solution(object):
    def pivotIndex(self, nums):
        leftsum = 0
        sums = sum(nums)
        for i in range (len(nums)):
            if leftsum == sums - leftsum - nums[i]:
                return i
            leftsum += nums[i]
        return -1
            


            
        

def main():
    sol = Solution()     
    print(sol.pivotIndex([-1,-1,-1,-1,-1,0])) 
    

if __name__ == "__main__":
    main()