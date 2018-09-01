class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # # Original solution (time limit exceeded)
        # x = [str(i) for i in str(s)]
        # max_length = 0
        # rep_index = 0
        # for i in range(len(x)):
        #     substr = []
        #     for j in x[i + rep_index:]:
        #         if j not in substr:
        #             substr.append(j)
        #         else:
        #             rep_index += substr.index(j)
        #             break
        #     length = len(substr)
        #     max_length = max(max_length, length)
        #     if substr == []:
        #         break
        #     elif len(substr) == len(x[i + rep_index:]):
        #         break
        #     else:
        #         pass
        # return max_length

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
