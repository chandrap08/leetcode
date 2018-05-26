class Solution(object):
    def longest_string(self, s):
        long_list = []
        for a in s:
            i = s.index(a)
            s1 = s[i + 1:]
            longString = a
            print "A is %s" % a
            for b in s1:
                print "B is %s" % b
                if a != b and b not in longString:
                    print "No match"
                    longString = longString + b
                    long_list.append(longString)
                    # print longString
                else:
                    print "match"
                    # long_list.append(longString)
                    break

        g = list(map(lambda x: len(x), long_list))
        return max(g)


if __name__ == "__main__":
    s = Solution()
    input = "pkewwas"
    result = s.longest_string(input)
    g = list(map(lambda x: len(x), result))
    print max(g)