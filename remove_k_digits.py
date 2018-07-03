class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if len(num) == 1: return 0

        stack,last = [],0
        nums = list(num)
        stack.append(nums[0])
        for i in range(1,len(nums)):
            if k == 0:
                break
            if nums[i] < stack[-1]:
                stack.pop()
                k -= 1
            else:
                break
            stack.append(nums[i])
            last = i
            print(stack)
        stack += nums[last+1:]
        while k != 0:
            stack.pop()
            k -= 1
        for i in range(len(stack)):
            if stack[i] !='0':
                break
        stack = stack[i:]

        if not stack: return 0
        return ''.join(stack)

if __name__ == "__main__":
    s = Solution()
    num = "1234567890"
    k = 9
    print(s.removeKdigits(num,k))