class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        mid = int(len(numbers)/2)
        if target < numbers[-1] and target >= numbers[mid]:
            i = mid
            while target <= numbers[i]:
                i += 1
        elif target < numbers[mid]:
            i = mid
            while target <= numbers[i]:
                i -= 1

        for j in range(i):
            for k in range(j+1,len(numbers)):
                if numbers[j] + numbers[k] == target:
                    return [j+1,k+1]

if __name__ == "__main__":
    s = Solution()
    numbers = [-1,0]
    target = -1
    print(s.twoSum(numbers,target))