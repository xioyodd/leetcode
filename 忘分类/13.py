class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        s = s[::-1]
        pre_ch_val = 0
        ret = 0
        for ch in s:
            val = roman_map[ch]
            if val >= pre_ch_val:
                ret += val
            elif val < pre_ch_val:
                ret -= val
            pre_ch_val = val
        return ret