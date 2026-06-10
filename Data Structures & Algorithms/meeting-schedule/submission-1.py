"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sorted_interval = sorted(intervals, key = lambda a: (a.start, a.end))
        last = -1
        for interval in sorted_interval:
            if interval.start < last:
                return False
            last = interval.end
        return True

