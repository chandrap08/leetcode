import collections
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = collections.Counter(s)
        stack = []
        seen = set()
        for c in s:
            count[c] -= 1
            if c not in seen:
                while stack and stack[-1] > c and count[stack[-1]]:
                    seen.remove(stack.pop())
                seen.add(c)
                stack.append(c)
        return ''.join(stack)

if __name__ == "__main__":
    s = Solution()
    s.removeDuplicateLetters("abacf")



