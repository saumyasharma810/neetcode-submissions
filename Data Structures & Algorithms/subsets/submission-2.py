class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset_lst = [[]]
        for i in range(len(nums)):
            new_subset_lst = []
            for subset in subset_lst:
                subset_copy = []
                subset_copy = subset[:]
                subset_copy.append(nums[i])
                new_subset_lst.append(subset)
                new_subset_lst.append(subset_copy)
            subset_lst = new_subset_lst
        return subset_lst

        