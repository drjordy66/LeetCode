class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == '':
            final_mapping = []
        else:
            x = [i for i in digits]
            two = ['a', 'b', 'c']
            thr = ['d', 'e', 'f']
            fou = ['g', 'h', 'i']
            fiv = ['j', 'k', 'l']
            six = ['m', 'n', 'o']
            sev = ['p', 'q', 'r', 's']
            eig = ['t', 'u', 'v']
            nin = ['w', 'x', 'y', 'z']
            letters = [[], [], two, thr, fou, fiv, six, sev, eig, nin]

            all_letters = []
            for i in x:
                all_letters.append(letters[int(i)])

            mapping = [[]]
            for i in all_letters:
                temp = []
                for j in i:
                    for k in mapping:
                        temp.append(k + [j])
                mapping = temp

            # Using a list comprehension
            # for i in all_letters:
            #     mapping = [k + [j] for j in i for k in mapping]

            final_mapping = []
            for i in mapping:
                final_mapping.append(''.join(i))
                
        return final_mapping
