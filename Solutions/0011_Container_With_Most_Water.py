class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        most_water = 0
        a_left = 0
        a_right = len(height) - 1
        while a_left < a_right:
            water = min(height[a_left], height[a_right]) * (a_right - a_left)
            most_water = max(most_water, water)
            if height[a_left] < height[a_right]:
                a_left += 1
            else:
                a_right -= 1
        return most_water
