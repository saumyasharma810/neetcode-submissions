class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for word in strs:
            encoded_str += str(len(word))+"#"+word
        return encoded_str

        4#abcd4




    def decode(self, s: str) -> List[str]:
        str_list = []
        i = 0
        while i < len(s):
            j = i
            while s[j]!='#':
                j+=1
            numb = int(s[i:j])
            word = s[j+1:j+numb+1]
            str_list.append(word)
            i = j+numb+1
        return str_list






