class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        I = 1
        V = 5
        X = 10
        L = 50
        C = 100
        D = 500
        M = 1000
        
        s_list = [i for i in s]
        j = 0
        number = 0
        
        while j < len(s_list):
            if s_list[j] == 'I':
                if len(s_list) > j+1 and s_list[j+1] == 'I':
                    if len(s_list) > j+2 and s_list[j+2] == 'I':
                        number += 3
                        j += 3
                    else:
                        number += 2
                        j += 2
                elif len(s_list) > j+1 and s_list[j+1] == 'V':
                    number += 4
                    j += 2
                elif len(s_list) > j+1 and s_list[j+1] == 'X':
                    number += 9
                    j += 2
                else:
                    number += 1
                    j += 1
            elif s_list[j] == 'X':
                if len(s_list) > j+1 and s_list[j+1] == 'X':
                    if len(s_list) > j+2 and s_list[j+2] == 'X':
                        number += 30
                        j += 3
                    else:
                        number += 20
                        j += 2
                elif len(s_list) > j+1 and s_list[j+1] == 'L':
                    number += 40
                    j += 2
                elif len(s_list) > j+1 and s_list[j+1] == 'C':
                    number += 90
                    j += 2
                else:
                    number += 10
                    j += 1
            elif s_list[j] == 'C':
                if len(s_list) > j+1 and s_list[j+1] == 'C':
                    if len(s_list) > j+2 and s_list[j+2] == 'C':
                        number += 300
                        j += 3
                    else:
                        number += 200
                        j += 2
                elif len(s_list) > j+1 and s_list[j+1] == 'D':
                    number += 400
                    j += 2
                elif len(s_list) > j+1 and s_list[j+1] == 'M':
                    number += 900
                    j += 2
                else:
                    number += 100
                    j += 1
            elif s_list[j] == 'V':
                number += 5
                j += 1
            elif s_list[j] == 'L':
                number += 50
                j += 1
            elif s_list[j] == 'D':
                number += 500
                j += 1
            elif s_list[j] == 'M':
                number += 1000
                j += 1
            
        return number
