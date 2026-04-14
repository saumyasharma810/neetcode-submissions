class Solution:
    def isValid(self, s: str) -> bool:
        leftBracks = []
        brackets = {'(':')','{':'}','[':']'}
        for char in s:
            if char in brackets.keys():
                leftBracks.append(char)
            else:
                if (not leftBracks) or (brackets[leftBracks.pop()] != char):
                    return False
        return not leftBracks



        