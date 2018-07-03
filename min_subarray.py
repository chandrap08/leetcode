class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        if len(nums) == 0: return 0
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == s: return 1
            dp[i] = dp[i-1] + nums[i]
        stack = []
        if dp[0] >= s: return 1
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if (dp[j] - dp[i] + nums[i]) >= s:
                    stack.append( j - i + 1)
        print(stack)
        return min(stack)

if __name__ == "__main__":

    s = 6
    nums = [10,2,3]
    print(Solution().minSubArrayLen(s,nums))