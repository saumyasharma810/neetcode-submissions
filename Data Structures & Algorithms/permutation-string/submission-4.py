class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_freq = [0] * 26
        s2_freq = [0] * 26
        matches = 0

        for i in range(len(s1)):
            s1_freq[ord(s1[i])-ord('a')]+=1
            s2_freq[ord(s2[i])-ord('a')]+=1

        for i in range(26):
            if s1_freq[i] == s2_freq[i]:
                matches+=1
        
        l,r = 0,len(s1)
        while r < len(s2):
            if matches == 26:
                return True
            first = ord(s2[l])-ord('a')
            last = ord(s2[r])-ord('a')
            
            s2_freq[last]+=1
            if s2_freq[last]==s1_freq[last]:
                matches+=1
            elif s2_freq[last] - 1 == s1_freq[last]:
                matches-=1
            
            s2_freq[first]-=1
            if s2_freq[first]==s1_freq[first]:
                matches+=1
            elif s2_freq[first] + 1 == s1_freq[first]:
                matches-=1
            r+=1
            l+=1
        return matches == 26




        