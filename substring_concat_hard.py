from functools import reduce
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        substringIndex = []
        len_w = len(words[0])
        if len(words) > 0 and len(s)> 0:
            #word_length = reduce(lambda x,y:x+y,[len(w) for w in words])
            word_length = len_w * len(words)
            #print(word_length)
            for i in range(len(s)-word_length+1):
                count = 0
                s1 = s[i:i + word_length]
                s1List = [s1[x:x+len_w] for x in range(0,len(s1),len_w)]
                #print(s1List)
                for w in words:
                    if w in s1List:
                        count += 1
                        s1List.remove(w)
                        #s1 = s1[:s1.index(w)] + s1[s1.index(w)+len(w):]
                        #print("reduced s %s removed %s" % (s1,w))
                if count == len(words):
                    substringIndex.append(i)
        return substringIndex

if __name__ == "__main__":
    s = Solution()
    print(s.findSubstring("ababaab",["ab","ba","ba"]))