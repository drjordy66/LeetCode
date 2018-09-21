class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            y = -1*x
            separate = [int(i) for i in str(y)]
            separate.reverse()
            merge = int(''.join(map(str, separate)))
            merge = -1*merge
        else:
            separate = [int(i) for i in str(x)]
            separate.reverse()
            merge = int(''.join(map(str, separate)))

        if (merge > -1*(2**31)) & (merge < (2**31)-1):
            return merge
        else:
            return 0
