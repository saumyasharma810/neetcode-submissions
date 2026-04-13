class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_freq = [0] * 26
        s2_freq = [0] * 26
        l,r = 0,len(s1)
        for i in range(len(s1)):
            s1_freq[ord(s1[i])-ord('a')]+=1
            s2_freq[ord(s2[i])-ord('a')]+=1
        while r < len(s2):
            print(s1_freq, s2_freq)
            if s1_freq == s2_freq:
                return True
            else:
                s2_freq[ord(s2[l])-ord('a')]-=1
                s2_freq[ord(s2[r])-ord('a')]+=1
                r+=1
                l+=1
        if s1_freq == s2_freq:
            return True
        return False



        