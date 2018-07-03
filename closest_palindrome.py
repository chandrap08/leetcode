class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        #a = list(n)
        #c = False
        i = 1
        while True:
            n_right = int(n) + i
            n_left = int(n) - i
            if str(n_left) == ''.join(list(reversed(str(n_left)))):
                return str(n_left)
            elif str(n_right) == ''.join(list(reversed(str(n_left)))):
                return str(n_right)
            i += 1

if __name__ == "__main__":
    s = Solution()
    print(s.nearestPalindromic("1325060231"))

