class Solution:
    def checkValidString(self, s: str) -> bool:
        # forward pass
        i = 0
        stack = []
        stars = 0
        while i < len(s):
            if s[i] == '(':
                stack.append('(')
            elif s[i] == ')':
                if len(stack) > 0:
                    stack.pop()
                elif stars > 0:
                    stars-=1
                else:
                    return False
            else:
                stars+=1
            i+=1
        #backward pass
        i = len(s)-1
        stack = []
        stars = 0
        while i > -1:
            if s[i] == ')':
                stack.append(')')
            elif s[i] == '(':
                if len(stack) > 0:
                    stack.pop()
                elif stars > 0:
                    stars-=1
                else:
                    return False
            else:
                stars+=1
            i-=1
        return True





        