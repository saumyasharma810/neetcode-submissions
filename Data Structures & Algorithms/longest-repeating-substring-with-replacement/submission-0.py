class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0,0
        freq = [0] * 26
        maxi = -1
        while r < len(s):
            freq[ord(s[r])-ord('A')]+=1
            while r - l + 1 - max(freq) > k:
                freq[ord(s[l])-ord('A')]-=1
                l+=1
            maxi = max(maxi, r-l+1)
            r+=1
        return maxi
            



        