class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grpAna = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in grpAna:
                grpAna[sorted_word].append(word)
            else:
                grpAna[sorted_word] = [word]
        return [y for x,y in grpAna.items()]
