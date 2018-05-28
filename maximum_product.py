class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)

        max_list = []
        max_list.append(int(nums[-1]) * int(nums[-2]) * int(nums[-3]))
        max_list.append(int(nums[0]) * int(nums[1]) * int(nums[2]))
        max_list.append(int(nums[0]) * int(nums[1]) * int(nums[-1]))
        max_list.append(int(nums[0]) * int(nums[-1]) * int(nums[-2]))

        return max(max_list)

if __name__ == "__main__":
    s = Solution()
    print(s.maximumProduct([9,1,5,6,7,2]))