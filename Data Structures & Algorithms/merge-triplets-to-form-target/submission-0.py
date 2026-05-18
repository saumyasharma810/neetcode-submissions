class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found = [False, False, False]
        for triple in triplets:
            if triple[0] > target[0] or triple[1] > target[1] or triple[2] > target[2]:
                continue
            if triple[0] == target[0]:
                found[0] = True
            if triple[1] == target[1]:
                found[1] = True
            if triple[2] == target[2]:
                found[2] = True
        return found[0] and found[1] and found[2]

        