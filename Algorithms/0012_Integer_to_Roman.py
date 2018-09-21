class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        num_list = [int(i) for i in str(num)]
        num_length = len(num_list)
        j = 0
        roman = ''
        
        if num_length == 4:
            if num_list[0] == 3:
                roman += 'MMM'
            elif num_list[0] == 2:
                roman += 'MM'
            else:
                roman += 'M'
        else:
            pass

        if num_length >= 3:
            if num_list[num_length - 3] == 9:
                roman += 'CM'
            elif num_list[num_length - 3] == 8:
                roman += 'DCCC'
            elif num_list[num_length - 3] == 7:
                roman += 'DCC'
            elif num_list[num_length - 3] == 6:
                roman += 'DC'
            elif num_list[num_length - 3] == 5:
                roman += 'D'
            elif num_list[num_length - 3] == 4:
                roman += 'CD'
            elif num_list[num_length - 3] == 3:
                roman += 'CCC'
            elif num_list[num_length - 3] == 2:
                roman += 'CC'
            elif num_list[num_length - 3] == 1:
                roman += 'C'
            else:
                pass
        else:
            pass
        
        if num_length >= 2:
            if num_list[num_length - 2] == 9:
                roman += 'XC'
            elif num_list[num_length - 2] == 8:
                roman += 'LXXX'
            elif num_list[num_length - 2] == 7:
                roman += 'LXX'
            elif num_list[num_length - 2] == 6:
                roman += 'LX'
            elif num_list[num_length - 2] == 5:
                roman += 'L'
            elif num_list[num_length - 2] == 4:
                roman += 'XL'
            elif num_list[num_length - 2] == 3:
                roman += 'XXX'
            elif num_list[num_length - 2] == 2:
                roman += 'XX'
            elif num_list[num_length - 2] == 1:
                roman += 'X'
            else:
                pass
        else:
            pass

        if num_length >= 1:
            if num_list[num_length - 1] == 9:
                roman += 'IX'
            elif num_list[num_length - 1] == 8:
                roman += 'VIII'
            elif num_list[num_length - 1] == 7:
                roman += 'VII'
            elif num_list[num_length - 1] == 6:
                roman += 'VI'
            elif num_list[num_length - 1] == 5:
                roman += 'V'
            elif num_list[num_length - 1] == 4:
                roman += 'IV'
            elif num_list[num_length - 1] == 3:
                roman += 'III'
            elif num_list[num_length - 1] == 2:
                roman += 'II'
            elif num_list[num_length - 1] == 1:
                roman += 'I'
            else:
                pass
        else:
            pass
        
        return roman
