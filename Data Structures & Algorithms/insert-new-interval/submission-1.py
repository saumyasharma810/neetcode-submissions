class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            i+=1
        j = len(intervals)-1
        while j >= 0 and intervals[j][0] > newInterval[1]:
            j-=1
        # if i>j:
        #     intervals.insert(i, newInterval)
        #     print(intervals)
        #     return intervals
        # intervals[i:j+1] = [min(intervals[i][0], newInterval[0]), max(intervals[j][1], newInterval[1])]
        new_intervals = intervals[0:i]
        first = newInterval[0]
        if i < len(intervals):
            first = min(intervals[i][0], first)
        second = newInterval[1]
        if j >= 0:
            second = max(second, intervals[j][1])
        new_intervals.append([first,second])
        new_intervals += intervals[j+1:]
        # new_intervals = [intervals[0:i] + [min(intervals[i][0], newInterval[0]), max(intervals[j][1], newInterval[1])] + intervals[j+1:]]
        # print(new_intervals)
        return new_intervals

        

