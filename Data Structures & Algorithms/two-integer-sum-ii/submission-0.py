class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers_with_index = [(n,i+1) for i,n in enumerate(numbers)]
        numbers_sorted = sorted(numbers_with_index)
        i,j = 0,len(numbers)-1
        while i<j:
            if numbers_sorted[i][0] + numbers_sorted[j][0] < target:
                i+=1
            elif numbers_sorted[i][0] + numbers_sorted[j][0] > target:
                j-=1
            else:
                return [min(numbers_sorted[i][1], numbers_sorted[j][1]), max(numbers_sorted[i][1], numbers_sorted[j][1])]

        return []

        