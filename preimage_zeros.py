from functools import reduce
class Solution(object):
    def preimageSizeFZF(self, K):
        """
        :type K: int
        :rtype: int
        """
        fact = 0
        dict_k = {}
        fact_dict = {}
        if K == 0: return 5
        elif len(dict_k) > 0:
            if K > max(dict_k.keys()):
                start = dict_k[max(dict_k.keys())]
        else:
            start = 5
        for i in range(start,K*10):
            if i-1 not in fact_dict.keys():
                p = reduce(lambda x,y: x*y,range(1,i))
                fact_dict[i] = p
            else:
                p = fact_dict[i-1] * (i+1)
            print(p)
            j,count = 1,0
            while (str(p)[-j] == '0'):
                count += 1
                j += 1
            if count == K:
                fact += 1
            dict_k[K] = i
        return fact

if __name__ == "__main__":
    s = Solution()
    K = 79
    print(s.preimageSizeFZF(K))

