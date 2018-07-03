class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        max_list = []
        if len(nums1) > 0 and len(nums2) > 0:
            if len(nums1) + len(nums2) == k:
                if nums1[0] >= nums2[0]:
                    return nums1 + nums2
                else:
                    return nums2 + nums1
            else:
                while k > 0:
                    print(nums1,nums2)
                    if len(nums1) > 0 and len(nums2) > 0:
                        if max(nums1) > max(nums2):
                            max_list.append(max(nums1))
                            nums1 = nums1[nums1.index(max(nums1)):]
                            del nums1[0]
                        else:
                            max_list.append(max(nums2))
                            nums2 = nums2[nums2.index(max(nums2)):]
                            del nums2[0]
                            #print(nums2)
                    elif len(nums1) > 0:
                        max_list.append(max(nums1))
                        nums1 = nums1[nums1.index(max(nums1)):]
                        del nums1[0]
                    elif len(nums2) > 0:
                        max_list.append(max(nums2))
                        nums2 = nums2[nums2.index(max(nums2)):]
                        del nums2[0]
                    k -= 1
        elif len(nums1) > 0: max_list = nums1
        else: max_list = nums2
        return max_list

if __name__ == "__main__":
    s = Solution()
    nums1 = [3,9]
    nums2 = [8,9]
    k = 3
    print(s.maxNumber(nums1,nums2,k))