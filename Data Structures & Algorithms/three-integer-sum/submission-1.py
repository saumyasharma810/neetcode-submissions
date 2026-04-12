class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_sort = sorted(nums)
        sums = list()
        i = 0
        # -4 -1 -1 0 1 2
        while i < len(nums)-2:
            j,k = i+1, len(nums)-1
            while j<k :
                if nums_sort[j] + nums_sort[k] + nums_sort[i] < 0:
                    j+=1
                elif nums_sort[j] + nums_sort[k] + nums_sort[i] > 0:
                    k-=1
                else:
                    sums.append([nums_sort[i], nums_sort[j], nums_sort[k]])
                    j+=1
                    k-=1
                    while j < k and nums_sort[j]==nums_sort[j-1]:
                        j+=1
            i+=1
            while i < len(nums)-2 and nums_sort[i] == nums_sort[i-1]:
                i+=1

                
        return sums

        