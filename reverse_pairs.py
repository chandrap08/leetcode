from collections import Counter
class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        reverse_pairs = []
        if len(nums) == 2:
            if nums[0] > nums[1] * 2:
                return 1
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] > 2*nums[j]:
                    reverse_pairs.append(nums[i])

        print(Counter(reverse_pairs))
        return (sum(Counter(reverse_pairs).values()))

if __name__ == "__main__":
    s = Solution()
    print(s.reversePairs([2147483647,2147483647,-2147483647,-2147483647,-2147483647,2147483647]))