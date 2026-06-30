class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def palindrome(i,j):
            while i < j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True

        def get_remaining(i):
            if i == len(s):
                return (True,[[]])
            lst = []
            for j in range(i,len(s)):
                possible, remaining_lst = get_remaining(j+1)
                if palindrome(i,j) and possible: # j included
                    # print(i)
                    for items in remaining_lst:
                        lst.append([s[i:j+1]]+items)
                    # print(lst)
            if lst:
                return (True,lst)
            return (False, [])
        
        # print(get_remaining(0)[1])

        return get_remaining(0)[1]