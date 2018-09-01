class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        x = [str(i) for i in str(s)]
        max_length = 0
        substr = []
        for i in x:
            if i not in substr:
                substr.append(i)
            else:
                del substr[0:substr.index(i) + 1]
                substr.append(i)
            max_length = max(max_length, len(substr))
        return max_length
