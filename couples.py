class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        couples = {}
        for i in range(0,len(row),2):
            couples[i] = i+1
            couples[i+1] = i
        j = 0
        swaps = 0
        while j < len(row):
            if row[j] != couples[row[j+1]]:
                p = row[j+1]
                po = row.index(couples[row[j]])
                row[j+1] = row[po]
                row[po] = p
                swaps += 1
                #print(row)
            j += 2
        return swaps

if __name__ == "__main__":
    s = Solution()
    print(s.minSwapsCouples([3, 2, 0, 1]))
