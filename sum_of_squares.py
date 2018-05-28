import math
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        print c
        if c > 0:
            squareLimit = int(math.sqrt(c)) + 1
            for i in range(1,squareLimit+1):
               if i**2 <= c:
                   r = math.sqrt(c - i**2)
                   if r.is_integer():
                       return True
               else:
                return False
            return False
        else:
            return True

if __name__ == "__main__":
    s = Solution()
    print(s.judgeSquareSum(100000000))