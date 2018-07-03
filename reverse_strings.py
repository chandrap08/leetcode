class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        l = s.split(" ")
        rev = []
        print(l)
        for i in l[::-1]:
            if i != "":
                rev.append(i)
        return " ".join(rev)

if __name__ == "__main__":
    print(Solution().reverseWords("the sky is blue"))
