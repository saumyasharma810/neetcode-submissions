class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        new_nums = sorted(nums)
        def subsets(i):
            nonlocal ans
            new_lst = []
            for sets in ans:
                new_lst.append(sets)
                new_sets = sets.copy()
                new_sets.append(new_nums[i])
                new_lst.append(new_sets)
            ans = new_lst
        for i in range(len(nums)):
            subsets(i)
        unique = set()
        for a in ans:
            unique.add(tuple(a))
        new_ans = []
        for a in unique:
            new_ans.append(list(a))
        return new_ans



        
        