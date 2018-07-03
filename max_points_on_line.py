# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b
from collections import defaultdict,Counter

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        slopes = []
        ps = [(x[0], x[1]) for x in points]
        a = list(Counter(ps))
        for i in range(len(a)-1):
            s = Counter()
            #s_set.add(points[i])
            for p in range(i+1,len(a)):
                if a[p][1] == a[i][1]:
                    slope = 0
                elif a[p][0] == a[i][0]:
                    slope = 1
                else:
                    slope = (a[p][1] - a[i][1])/(a[p][0] - a[i][0])
                s[slope] += 1
                slopes.append(s.most_common(1)[0][1])
        print(s)
        return max(slopes) + 1

        # max_points = []
        # for k,v in s.items():
        #     max_p = {}
        #     for x in v:
        #         if x not in max_p:
        #             max_p[x] = 1
        #         else:
        #             max_p[x] += 1
        #     max_points.append(max(max_p.values()))
        #     print(max_p)
        # #print(max_points)
        # max_points = max(max_points) + 1
        # return max_points

if __name__ == "__main__":
    s = Solution()
    l= [[0,0],[1,1],[0,0]]

    print(s.maxPoints(points = l))