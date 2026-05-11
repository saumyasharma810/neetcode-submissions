class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_length = 0
        max_l_str = ""
        for i in range(len(s)):
            # odd
            j,k = i,i
            while j >=0 and k < len(s) and s[j]==s[k]:
                j-=1
                k+=1
            if (k-j-1) > max_length:
                max_length = (k-j-1)
                max_l_str = s[j+1:k]
            # even
            j,k = i,i+1
            while j >=0 and k < len(s) and s[j]==s[k]:
                j-=1
                k+=1
            if (k-j-1) > max_length:
                max_length = (k-j-1)
                max_l_str = s[j+1:k]
        return max_l_str


        