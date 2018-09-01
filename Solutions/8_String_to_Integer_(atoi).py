class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        x = [i for i in str]
        numlist = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '+']
        numlist2 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        integer = []
        str_to_int = 0

        for j in x:
            if j == ' ':
                pass
            elif j in numlist:
                for k in x[x.index(j):]:
                    if k in numlist and integer == []:
                        integer.append(k)
                    elif k in numlist2:
                        integer.append(k)
                    else:
                        break
                if integer == [] or integer == ['-'] or integer == ['+']:
                    break
                else:
                    str_to_int = int(''.join(integer))
                    break
            else:
                break

        if str_to_int < -1*(2**31):
            return -1*(2**31)
        elif str_to_int > 2**31-1:
            return 2**31-1
        else:
            return str_to_int
