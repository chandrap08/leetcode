class Solution(object):

    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """

        lines,c = [],0
        while c <= len(words)-1:
            l,c = Solution().fillLine(c,maxWidth,words)
            lines.append(l)
            c += 1
        #print(lines)
        p = ','.join('\"' + line + '\"' for line in lines)
        return p

    def fillLine(self,c,maxWidth,words):
        remainder = maxWidth
        line,gaps = [],0
        #print("start here",c,len(words),len(words[c]))
        if c == len(words) -1:
            if remainder > len(words[c]):
                line.append(words[c])
            return ''.join(line), c
        else:
            while remainder > len(words[c]):
                if c < len(words) -1:
                    remainder = remainder - len(words[c]) -1
                    line.append(words[c])
                    line.append(" ")
                    #print(line,remainder,c)
                    c += 1

        gaps = int(remainder/len(line)-1)
        line_1 = []
        for li in line[:-1]:
            line_1.append(li + " "* gaps)

        if remainder%(len(line)-1) == 0:

            line_1 += line[-1]
        else:

            line_1 = [line_1[0], [" "]*(remainder%(len(line)-1))] + line_1[1:]

        return ''.join(line_1),c-1

if __name__ == "__main__":
    s = Solution()
    words,maxWidth = ["This", "is", "an", "example", "of", "text", "justification."],16
    print(s.fullJustify(words,maxWidth))


