class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            if (target-nums[i]) in (nums[:i] + nums[i+1:]):
                return [i, (nums[:i] + nums[i+1:]).index(target-nums[i]) + 1]
            else:
                pass