class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        closest = nums[0] + nums[1] + nums[2]
        nums = sorted(nums)
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                sum3 = nums[l] + nums[r] + nums[i]
                if abs(target - sum3) < abs(target - closest):
                    closest = sum3
                else:
                    pass
                if sum3 < target:
                    l += 1
                else:
                    r -= 1
        return closest
