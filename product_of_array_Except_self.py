class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p = []
        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if i != j:
                    prod *= nums[j]
            p.append(prod)
        return p

if __name__ == "__main__":
    s = Solution()
    print(s.productExceptSelf([1,2,3,4]))