class Solution(object):
    def kSimilarity(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        no_similar = []
        A,B = list(A),list(B)
        for i in range(len(A)):
            if A[i] != B[i]:
                no_similar.append(i)
        count = 0
        while no_similar:
            print(len(no_similar))
            for s in range(len(no_similar)):
                b_ind = B.index(A[no_similar[s]])
                p = A[b_ind]
                A[b_ind] = A[no_similar[s]]
                A[no_similar[s]] = p
                del no_similar[s]
                count += 1

        return count

if __name__ == "__main__":
    s = Solution()
    print(s.kSimilarity(A = "aabc", B = "abca"))


