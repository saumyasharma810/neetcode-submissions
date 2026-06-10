"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda a: (a.start, a.end))
        pq = []
        rooms = 0
        for interval in intervals:
            if len(pq) > 0 and interval.start >= pq[0]:
                heapq.heappop(pq)
                heapq.heappush(pq,interval.end) 
            else:
                heapq.heappush(pq,interval.end)
                rooms+=1
        return rooms
        


        