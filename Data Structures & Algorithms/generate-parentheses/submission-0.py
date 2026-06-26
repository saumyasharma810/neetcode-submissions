class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        combs = set()

        def combis(length, open_brack, string):
            if length == 2*n:
                if open_brack == length/2:
                    combs.add(string)
                return 
            close_brack = length-open_brack
            if close_brack == open_brack:
                combis(length+1, open_brack+1, string+'(')
                return
            combis(length+1, open_brack, string+')')
            combis(length+1, open_brack+1, string+'(')
        
        combis(1,1,'(')

        return [s for s in combs]
        