class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sub_str = defaultdict(int)
        diff = 0
        for char in t:
            if sub_str[char] == 0:
                diff += 1
            sub_str[char] += 1
        new_dict = defaultdict(int)
        l,r = 0,0
        min_len = float("inf")
        min_str = ""
        while r < len(s):
            if s[r] in sub_str:
                new_dict[s[r]] += 1
                if new_dict[s[r]] == sub_str[s[r]]:
                    diff-=1
            while diff == 0 and l <= r:
                if r-l+1 < min_len:
                    min_str = s[l:r+1]
                    min_len = r-l+1
                if s[l] in sub_str:
                    new_dict[s[l]] -= 1
                    if new_dict[s[l]] < sub_str[s[l]]:
                        diff+=1
                l+=1
            r+=1
        return min_str
            


            

        
        