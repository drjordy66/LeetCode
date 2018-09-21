class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ''
        else:
            longest = [str(i) for i in strs[0]]
            for word in strs[1:]:
                new_longest = []
                letters = [str(i) for i in word]
                length = min(len(longest), len(letters))
                for i in range(0, length):
                    if longest[i] == letters[i]:
                        new_longest.append(letters[i])
                    else:
                        break
                longest = new_longest
            return ''.join(longest)
