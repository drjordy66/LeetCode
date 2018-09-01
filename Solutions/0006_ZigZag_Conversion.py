class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        x = [str(i) for i in s]
        new_s = []
        for row in range(1, numRows + 1):
            next_s = row
            while next_s <= len(s):
                new_s.append(x[next_s - 1])
                if numRows == 1:
                    step_size = 1
                elif row == 1:
                    step_size = numRows*2 - 2
                elif row == numRows:
                    step_size = numRows*2 - 2
                else:
                    diag = numRows*2 - row*2
                    next_s += diag
                    if next_s <= len(s):
                        new_s.append(x[next_s - 1])
                    else:
                        break
                    cols = numRows*2 - 2
                    step_size = cols - diag
                next_s += step_size
        return ''.join(new_s)
