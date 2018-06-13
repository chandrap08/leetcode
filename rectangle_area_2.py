class Solution(object):
    def rectangleArea(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """

        current = rectangles[0]
        area = (current[2] - current[0]) * (current[3] - current[1])
        #print(area)
        for r in rectangles[1:]:
            area_sub = 0
            area += (r[2] - r[0])*(r[3] - r[1])
            #print area
            if r[2] >= current[2] and r[0] >= current[0]:
                if r[3] >= current[3] and r[1] <= current[3]:
                    area_sub = (current[3] - r[1]) * (current[2] - r[0])
            elif r[0] <= current[0] and r[2] >= current[0] and r[2] <= current[2]:
                if r[3] >= current[3] and r[1] <= current[3]:
                    area_sub = (current[3] - r[1]) * (r[1] - current[0])
            elif r[0] >= current[0] and r[2] <= current[2]:
                if r[1] >= current[1] and r[3] <= current[3]:
                    area_sub = (r[2] - r[0]) * (r[3] - r[1])
                elif r[1] >= current[1] and r[3] >= current[3]:
                    area_sub = (r[2] - r[0]) *(current[3] - r[1])
                elif r[1] <= current[1] and r[3] >= current[1]:
                    area_sub = (r[2] - r[0]) * (r[3] - current[1])
            print(area_sub)
            area -= area_sub
            current = r
            print(current)

        print(area)

if __name__ == "__main__":
    s = Solution()
    s.rectangleArea([[0,0,2,2],[1,0,2,3],[1,0,3,1]])