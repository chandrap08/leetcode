class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        gaps = []
        if len(nums) < 2:
            return 0
        else:
            for i in range(len(nums)-1):
                gaps.append(nums[i+1]-nums[i])
            return max(gaps)

if __name__ == "__main__":
    s = Solution()
    print(s.maximumGap([3,6,9,1]))