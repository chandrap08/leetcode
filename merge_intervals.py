#Definition for an interval.
class Interval(object):
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = intervals.sort(key=lambda x:x.start)
        merged = []
        for interval in intervals:
            if not merged or merged[-1].end < interval.start:
                merged.append(interval)
            else:
                merged[-1].end = max(merged[:-1].end,interval.end)
        return merged


if __name__ == "__main__":
    s = Solution()
    i1 = Interval(1,3)
    i2 = Interval(2,6)
    i3 = Interval(8,10)
    i4 = Interval(15,18)

    s.merge([i1,i2,i3,i4])
