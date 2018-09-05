class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        x = [i for i in s]
        if x != []:
            longest = x[0]
        else:
            longest = ''
        for i in range(len(x)):
            indices = [index for index, value in enumerate(x[i + 1:]) if value == x[i]]
            indices = [z + i + 1 for z in indices]
            for j in sorted(indices, reverse=True):
                if len(x[i:j + 1]) > len(longest):
                    forward = x[i:j + 1]
                    backward = x[i: j + 1]
                    backward.reverse()
                    if forward == backward:
                        longest = ''.join(forward)
                        break
                    else:
                        pass
                else:
                    break
            if len(longest) > len(x[i:]):
                break
            else:
                pass
        return longest
