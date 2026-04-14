class Solution:
    def isValid(self, s: str) -> bool:
        leftBracks = []
        opens = ['(','{','[']
        closing = [')','}',']']
        for char in s:
            if char in opens:
                leftBracks.append(char)
            else:
                ind = closing.index(char)
                if (not leftBracks) or (leftBracks.pop() != opens[ind]):
                    return False
        return not leftBracks



        