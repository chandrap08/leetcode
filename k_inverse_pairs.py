class Solution(object):
    def kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        a = range(1,n+1)
        combinations = 0
        if k == 0:
            combinations = 1
        elif k == 1:
            combinations = n-1
        elif k > n-1:
            combinations = 0
        elif (n - k) == 1:
            combinations = n - 1
        else:
            unpaired = n-k
            p = int(n/2) + int((n-1)/2)
            combinations = unpaired + p
        return combinations

if __name__ == "__main__":
    s = Solution()
    print(s.kInversePairs(3,2))