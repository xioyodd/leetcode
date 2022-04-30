# 给你一个字符串 s，找到 s 中最长的回文子串。
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindrome(i,j):
            while i>=0 and j<=len(s)-1 and s[i] == s[j]:
                i-=1
                j+=1
            return i+1,j
        def longer(l,r,start,end):
            if r-l > end-start:
                return l,r
            return start,end
        start = -1
        end = -1
        for i in range(len(s)):
            l,r = palindrome(i,i)
            start,end = longer(l,r,start,end)
            l,r = palindrome(i,i+1)# 为什么不会越界，因为palindrome()进去就判断了
            start, end = longer(l, r, start, end)
        return s[start:end]

if __name__ == '__main__':
    s = '1234'
    print(s[0])
    print(s[3])