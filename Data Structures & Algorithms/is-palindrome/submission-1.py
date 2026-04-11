class Solution:
    def isPalindrome(self, s: str) -> bool:
        wo_alpha = ""
        for char in s:
            if char.isalnum():
                wo_alpha += char
        wo_alpha = wo_alpha.lower()
        i, j = 0, len(wo_alpha)-1
        while i<j:
            if wo_alpha[i] != wo_alpha[j]:
                return False
            i+=1
            j-=1

        return True
        