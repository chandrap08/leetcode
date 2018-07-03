class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:return 0
        dp = [1,1]
        for i,x in enumerate(s):
            num = 0
            if x!='0':num+=dp[-1]
            if i>=1 and int(s[i-1:i+1])>=10 and int(s[i-1:i+1])<=26:num+=dp[-2]
            if not num:return 0
            dp.append(num)
            print(dp)
        return dp[-1]

if __name__ == "__main__":
    print(Solution().numDecodings("226"))



