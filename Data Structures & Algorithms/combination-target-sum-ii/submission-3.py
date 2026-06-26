class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        combs = set()
        candidates.sort()


        def combination(i, total, tup):
            if total == target:
                combs.add(tup)
                return
            if total > target or i >= len(candidates):
                return
            new_tup = tup + (candidates[i],)
            combination(i+1, total+candidates[i],new_tup)
            l = candidates[i]
            while i < len(candidates) and l == candidates[i]:
                i+=1
            combination(i, total, tup)
        
        empty_tup = tuple()
        combination(0,0,empty_tup)
        return [list(s) for s in combs]
            
        
        