class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = [-1] * 26
        for i,c in enumerate(s):
            last_index[ord(c)-ord('a')] = i
        grp = []
        l = 0
        last = 0
        while l < len(s):
            last = last_index[ord(s[l])-ord('a')]
            r = l
            while r < len(s) and r <= last:
                last = max(last, last_index[ord(s[r])-ord('a')])
                r+=1
            grp.append(r-l)
            l = r
        return grp
        
        




        