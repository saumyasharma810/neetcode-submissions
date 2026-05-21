class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if(len(s3) != len(s1) + len(s2)):
            return False

        dp = {}

        def possible(first, second):
            if first + second == len(s3):
                return True
            poss = False
            if (first,second) in dp:
                return dp[(first,second)]
            if first < len(s1) and s1[first] == s3[first+second]:
                poss = poss | possible(first+1, second)
            if second < len(s2) and s2[second] == s3[first+second]:
                poss = poss | possible(first, second+1)
            dp[(first,second)] = poss
            return poss

        return possible(0,0)
        