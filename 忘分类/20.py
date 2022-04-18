class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stk = []
        mp = {'[':0,']':0,'(':1,')':1,'{':2,'}':2}
        for ch in s:
            if ch == '[' or ch == '(' or ch == '{':
                stk.append(ch)
            elif len(stk) == 0 or mp[stk.pop()] != mp[ch]:
                    return False
        if len(stk) == 0:
            return True
        return False