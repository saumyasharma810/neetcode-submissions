class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        arr = [False] * (len(s)+1)
        arr[0] = True

        for i in range(1,len(s)+1):
            for word in wordDict:
                if arr[i-1] == True and word == s[i-1:(i-1)+len(word)]:
                    print(i,word)
                    arr[i+len(word)-1] = True


        return True if arr[len(s)] == True else False


        