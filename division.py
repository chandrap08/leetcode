class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend < 0 or divisor < 0:
            neg = True
        dividend,divisor = abs(dividend), abs(divisor)
        remainder = abs(dividend) - abs(divisor)
        if remainder < 0:
            return 0
        else:
            count = 0
            while remainder > 0:
                remainder = remainder - divisor
                count += 1

            if neg:
                return -(count)
            else:
                return count

if __name__ == "__main__":
    print(Solution().divide(dividend = 7, divisor = -3))