class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        if len(nums) == 0: return "0"
        if len(nums) == 1: return nums[0]
        stack = []
        stack.append(nums[0])
        for i in range(1,len(nums)):
            for j in range(len(stack)):
                if int(str(nums[i])[0]) > int(str(stack[j])[0]):
                    stack = stack[:j] + [nums[i]] + stack[j+1:]
                    print(stack)
                else:
                    stack.append(nums[i])

        stack = list(map(str,stack))
        return ''.join(stack)

if __name__ == "__main__":
    s = Solution()
    print(s.largestNumber([3,30,34,5,9]))

