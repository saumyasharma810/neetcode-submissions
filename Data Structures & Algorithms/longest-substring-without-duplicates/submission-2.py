class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        i,j = 0,0
        length = 0
        while j < len(s):
            if s[j] not in chars:
                chars.add(s[j])
                j+=1
            else:
                while s[i]!=s[j]:
                    chars.remove(s[i])
                    i+=1
                i+=1
                j+=1
            length = max(length, len(chars))
            
        return length



        