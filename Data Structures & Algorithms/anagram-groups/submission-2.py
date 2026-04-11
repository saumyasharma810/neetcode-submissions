class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grpAna = {}
        for word in strs:
            freq = [0] * 26
            for char in word:
                freq[ord(char)-ord('a')]+=1
            if tuple(freq) in grpAna:
                grpAna[tuple(freq)].append(word)
            else:
                grpAna[tuple(freq)] = [word]
                
        return [y for x,y in grpAna.items()]