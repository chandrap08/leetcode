from functools import reduce
class Solution(object):
    def splitArraySameAverage(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        avg  = reduce(lambda x,y: x+y,A)/len(A)
        A = sorted(A)
        B,C = [],[]
        sum = len(A)/2 * avg
        i,s = int(len(A)/2),sum
        if i % 2 == 0:
            for x in range(i,len(A),2):
                B.append(A[x])
                B.append(A[i - x])
                C.append(A[x+1])
                C.append(A[i - x +1])
                avg_B = reduce(lambda x, y: x + y, B) / len(B)
                avg_C = reduce(lambda x, y: x + y, C) / len(C)
                print(avg_B,avg_C)
                if avg_B == avg_C:
                    return True

        return False

if __name__ == "__main__":
    s = Solution()
    print(s.splitArraySameAverage([1,2,3,4,5,6,7,8]))

