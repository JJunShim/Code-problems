class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        i = l = 0 # i for first index, l for length

        for j in range(len(s)):
            if s[j-l: j+1] == s[j-l: j+1][::-1]: # compare with reversed substring
                i = j-l
                l += 1
            elif j-l > 0 and s[j-l-1: j+1] == s[j-l-1: j+1][::-1]:
                i = j-l-1
                l += 2

        return s[i: i+l]
