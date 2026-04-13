class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        for i in range(len(s)):
            while len(set(s[i:i+length])) == length:
                length+=1
        return max(0,length-1)
        