class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        sol_set = []
        for i in range(len(nums)):
            l_index = i + 1
            r_index = len(nums) - 1
            while l_index < r_index:
                if nums[l_index] + nums[r_index] < -nums[i]:
                    l_index += 1
                elif nums[l_index] + nums[r_index] > -nums[i]:
                    r_index -= 1
                else:
                    sol_set.append((nums[l_index], nums[r_index], nums[i]))
                    while l_index < r_index and nums[l_index] == nums[l_index + 1]:
                        l_index += 1
                    while l_index < r_index and nums[r_index] == nums[r_index - 1]:
                        r_index -= 1
                    l_index += 1
                    r_index -= 1
        sol_set = list(set(sol_set))
        return sol_set
