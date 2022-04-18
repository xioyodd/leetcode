class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        len_a = len(a)
        len_b = len(b)
        strlen = max(len_a, len_b)
        a = a.zfill(strlen)
        b = b.zfill(strlen)
        i = strlen-1
        carry = 0
        res = ''
        while i>=0:
            tmp = int(a[i]) + int(b[i]) + carry
            if tmp > 1:
                tmp -= 2
                carry = 1
            else:
                carry = 0
            res = str(tmp) + res
            i -= 1 
        if carry == 1:
            res = '1' + res
        return res
