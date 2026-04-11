class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for word in strs:
            encoded_str += '#'+str(len(word))+'#'+word
        return encoded_str




    def decode(self, s: str) -> List[str]:
        str_list = []
        i = 0
        while i < len(s):
            i+=1
            numb = ""
            while s[i]!='#':
                numb+=s[i]
                i+=1
            i+=1
            numb = int(numb)
            word = ""
            for j in range(numb):
                word+=s[i]
                i+=1
            str_list.append(word)
        return str_list






