class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0], x[1]))
        n = len(intervals)
        ans_array = [1] * n
        max_ans = 1
        for i in range(1,n):
            for j in range(0,i):
                if intervals[i][0] >= intervals[j][1]:
                    ans_array[i] = max(ans_array[j]+1, ans_array[i])
                    max_ans = max(max_ans, ans_array[i])
                    # print(i,j,max_ans)
        # print(ans_array)
        return n-max_ans
