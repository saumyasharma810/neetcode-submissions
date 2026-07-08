class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i = 0
        new_intervals = []
        curr_start, curr_end = -1,-1
        while i < len(intervals):
            if curr_start != -1 and (intervals[i][0] == curr_start or intervals[i][0] <= curr_end):
                # combine
                curr_end = max(intervals[i][1], curr_end)
            else:
                if curr_start != -1:
                    new_intervals.append([curr_start, curr_end])
                curr_start = intervals[i][0]
                curr_end = intervals[i][1]
            i+=1
        if curr_start!=-1:
            new_intervals.append([curr_start, curr_end])
        return new_intervals