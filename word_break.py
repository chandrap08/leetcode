from collections import defaultdict
class Solution(object):

        def wordBreak(self, s, wordDict):
            if len(wordDict):
                dp = defaultdict(list)
                maxlen = max(len(w) for w in wordDict)
                dp[0] = []
                res = []
                for i in range(1, len(s) + 1):
                    for j in range(i - maxlen, i):
                        print(j,i,s[j:i])
                        if j in dp and s[j:i] in wordDict:
                            #print(i,j)
                            dp[i].append(j)
                            print(list(dp))

                # print dp
                def unwind(k, sent):
                    if k in dp and len(dp[k]):
                        for i in dp[k]:
                            sent.append(s[i:k])
                            unwind(i, sent)
                            sent.pop()
                    elif len(sent):
                        res.append(' '.join(sent[::-1]))

                unwind(len(s), [])
                return res
            return []


if __name__ == "__main__":
    s = Solution()
    print(s.wordBreak("catsanddog",["cat", "cats", "and", "sand", "dog"]))
