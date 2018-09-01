class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y = [i for i in str(x)]
        y.reverse()
        try:
            y = int(''.join(y))
        except ValueError:
            pass
        return x == y
