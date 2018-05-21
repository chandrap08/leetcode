class Solution(object):
    def twosums(self,nums,target):
        for x in nums:
            j = target - x
            i = nums.index(x)
            if i == 0:
                n = nums[1:]
                if j in n:
                    rList = [nums.index(x), n.index(j) + 1]
                    return rList
            elif(i == len(nums) - 1):
                n = nums[:i]
                if j in n:
                    rList = [nums.index(x), n.index(j)]
                    return rList
            else:
                if (j in nums[:i]):
                    rList = [nums.index(x),nums[:1].index(j)]
                    return rList
                elif j in nums[i+1:]:
                    rList = [nums.index(x), nums[i+1:].index(j) + i + 1]
                    return rList

if __name__ == "__main__":
    nums = [2,5,5,11]
    #nums = [2,3,5,7]
    target = 10
    result = Solution().twosums(nums,target)
    print result